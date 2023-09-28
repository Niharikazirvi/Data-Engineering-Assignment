import pyspark.sql.functions as F


def extract_tour_operator_bookings(bookings_df):
    return bookings_df.filter(F.col("market_segment") == "Offline TA/TO")


def add_arrival_date(bookings_df):
    arrival_date_df = bookings_df.withColumn(
        "arrival_date", F.to_date(
            F.expr("concat(arrival_date_year, '-', arrival_date_month, '-', arrival_date_day_of_month)"), "yyyy-MMM-dd")
    )
    arrival_date_df.show()
    return arrival_date_df


def add_departure_date(bookings_df):
    # Cast the result of addition to int
    departure_date_df = bookings_df.withColumn(
        "departure_date",
        F.expr("date_add(arrival_date, cast(stays_in_weekend_nights as int) + cast(stays_in_week_nights AS int))")
    )

    return departure_date_df


def add_with_family_breakfast(bookings_df):
    with_family_breakfast_df = bookings_df.withColumn(
        "with_family_breakfast",
        F.when((F.col("children") + F.col("babies")) > 0, F.lit("Yes")).otherwise(F.lit("No"))
    )
    return with_family_breakfast_df
