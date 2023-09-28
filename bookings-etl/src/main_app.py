import logging
from pyspark.sql import SparkSession
from src.transformations import (
    extract_tour_operator_bookings,
    add_arrival_date,
    add_departure_date,
    add_with_family_breakfast
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def save_as_parquet(df, output_path):
    df.write.parquet(output_path, mode="overwrite")
    logger.info(f"Saved DataFrame to Parquet: {output_path}")


def main(spark: SparkSession, input_path: str, output_path: str):
    logger.info("Starting Spark ETL application...")

    # Read the CSV file
    bookings_df = spark.read.csv(input_path, header=True, inferSchema=True)
    logger.info(f"Read data from CSV file: {input_path}")
    bookings_df.show(2)

    # Extract tour operator bookings
    tour_operator_bookings_df = extract_tour_operator_bookings(bookings_df)

    # Add arrival date
    arrival_date_df = add_arrival_date(tour_operator_bookings_df)

    # Add departure date
    departure_date_df = add_departure_date(arrival_date_df)

    # Add with_family_breakfast
    with_family_breakfast_df = add_with_family_breakfast(departure_date_df)

    with_family_breakfast_df.show(2)
    final_df = with_family_breakfast_df.select(
        "hotel",
        "is_canceled",
        "lead_time",
        "arrival_date",
        "departure_date",
        "with_family_breakfast"
    )
    save_as_parquet(final_df, output_path)
    logger.info("Spark ETL application completed.")


if __name__ == "__main__":
    spark_session = SparkSession.builder \
        .appName("BookingsETL") \
        .config("spark.sql.legacy.timeParserPolicy", "LEGACY") \
        .getOrCreate()

    input_path = '../ETL-input/input_data.csv'
    output_path = '../ETL-output/output_data'

    main(spark_session, input_path, output_path)

    spark_session.stop()
