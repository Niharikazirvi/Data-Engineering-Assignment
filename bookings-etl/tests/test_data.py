import datetime

test_data_extract_tour_operator_bookings = [("Resort Hotel", 0, "Offline TA/TO"),
                                            ("City Hotel", 1, "Online TA")]

test_data_add_arrival_date = [(2022, "January", 1),
                              (2022, "February", 15)]

test_data_add_departure_date = [(datetime.date(2022, 1, 1), 1, 2),
                                (datetime.date(2022, 2, 15), 2, 3)]

test_data_add_with_family_breakfast = [(0, 0),
                                      (1, 2),
                                      (0, 1)]





# import datetime
#
# expected_csv_data = [{'hotel': 'Resort Hotel', 'is_canceled': '0', 'lead_time': '342'},
#  {'hotel': 'Resort Hotel', 'is_canceled': '0', 'lead_time': '737'},
#  {'hotel': 'Resort Hotel', 'is_canceled': '0', 'lead_time': '7'},
#  {'hotel': 'Resort Hotel', 'is_canceled': '0', 'lead_time': '13'}]
#
#
# test_arrival_departure_date = [
#     {
#         "arrival_date_year":"2022",
#         "arrival_date_month":"July",
#         "arrival_date_day_of_month":"2",
#         "stays_in_week_nights":"1",
#         "stays_in_weekend_nights":"2"
#     }
# ]
#
# expected_arrival_data = [
#     {
#         "arrival_date_year":"2022",
#         "arrival_date_month":"July",
#         "arrival_date_day_of_month":"2",
#         "stays_in_week_nights":"1",
#         "stays_in_weekend_nights":"2",
#         "arrival_date": datetime.date(2022, 7, 2)
#     }
# ]
#
# expected_arrival_departure_data = [
#     {
#         "arrival_date_year":"2022",
#         "arrival_date_month":"July",
#         "arrival_date_day_of_month":"2",
#         "stays_in_week_nights":"1",
#         "stays_in_weekend_nights":"2",
#         "arrival_date": datetime.date(2022, 7, 2),
#         "departure_date": datetime.date(2022, 7, 5)
#     }
# ]
#
# test_is_with_family_breakfast = [
#     {
#        "children":"2",
#        "babies":"0"
#     },
#     {
#        "children":"0",
#        "babies":"0"
#     }
# ]
#
# expected_is_with_family_breakfast = [
#     {
#        "children":"2",
#        "babies":"0",
#        "with_family_breakfast":"YES"
#     },
#     {
#        "children":"0",
#        "babies":"0",
#        "with_family_breakfast":"NO"
#     }
# ]