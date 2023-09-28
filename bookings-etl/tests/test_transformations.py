import unittest
import datetime

from pyspark.sql import SparkSession
from src.transformations import (
    extract_tour_operator_bookings,
    add_arrival_date,
    add_departure_date,
    add_with_family_breakfast
)
from .test_data import (
    test_data_extract_tour_operator_bookings,
    test_data_add_arrival_date,
    test_data_add_departure_date,
    test_data_add_with_family_breakfast
)

import sys

print("Worker Python Version:", sys.version)


class TestTransformations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.spark = SparkSession.builder \
            .appName("TestTransformations") \
            .config("spark.sql.legacy.timeParserPolicy", "LEGACY") \
            .getOrCreate()

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

    def test_extract_tour_operator_bookings(self):
        columns = ["hotel", "is_canceled", "market_segment"]
        test_df = self.spark.createDataFrame(test_data_extract_tour_operator_bookings, columns)

        result_df = extract_tour_operator_bookings(test_df)

        self.assertEqual(result_df.count(), 1)
        self.assertEqual(result_df.first()["hotel"], "Resort Hotel")
        self.assertEqual(result_df.first()["market_segment"], "Offline TA/TO")

    def test_add_arrival_date(self):
        columns = ["arrival_date_year", "arrival_date_month", "arrival_date_day_of_month"]
        test_df = self.spark.createDataFrame(test_data_add_arrival_date, columns)
        result_df = add_arrival_date(test_df)

        expected_dates = [datetime.date(2022, 1, 1), datetime.date(2022, 2, 15)]
        self.assertEqual(result_df.count(), len(expected_dates))
        self.assertEqual(result_df.collect()[0]["arrival_date"], expected_dates[0])
        self.assertEqual(result_df.collect()[1]["arrival_date"], expected_dates[1])

    def test_add_departure_date(self):
        columns = ["arrival_date", "stays_in_weekend_nights", "stays_in_week_nights"]
        test_df = self.spark.createDataFrame(test_data_add_departure_date, columns)
        result_df = add_departure_date(test_df)
        expected_dates = [datetime.date(2022, 1, 4), datetime.date(2022, 2, 20)]
        self.assertEqual(result_df.count(), len(expected_dates))
        self.assertEqual(result_df.collect()[0]["departure_date"], expected_dates[0])
        self.assertEqual(result_df.collect()[1]["departure_date"], expected_dates[1])

    def test_add_with_family_breakfast(self):
        columns = ["children", "babies"]
        test_df = self.spark.createDataFrame(test_data_add_with_family_breakfast, columns)

        result_df = add_with_family_breakfast(test_df)

        expected_values = ["No", "Yes", "Yes"]
        self.assertEqual(result_df.count(), len(expected_values))
        self.assertEqual(result_df.collect()[0]["with_family_breakfast"], expected_values[0])
        self.assertEqual(result_df.collect()[1]["with_family_breakfast"], expected_values[1])
        self.assertEqual(result_df.collect()[2]["with_family_breakfast"], expected_values[2])


if __name__ == '__main__':
    unittest.main()
