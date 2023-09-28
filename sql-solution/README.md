## Part 1 
### Problem 1
Write an Amazon Athena (or Presto) SQL query that creates a table from the reservations table,
that shows only the most recent state of each room that has not been reserved yet. Store the new
table in PARQUET data format and partition by checkin_date .

```
CREATE EXTERNAL TABLE room_recent_status as
(
    with latest_reservation_status as (
        SELECT ROW_NUMBER () OVER ( 
            PARTITION BY room_number
            ORDER BY checkout_date 
        ) row_number,room_number,reservation_status,checkin_date,checkout_date
        FROM reservations
        where reservation_status = 'OPEN' 
    ) select room_number,reservation_status,checkin_date,checkout_date
    from latest_reservation_status 
    where row_number = 1
)
PARTITIONED BY (checkin_date STRING)
STORED AS PARQUET
LOCATION 's3://given-bucket/location'
tblproperties ("parquet.compression"="SNAPPY");
```

### Problem 2 
Assuming that analysts and data consultants often filter on the reservation_status column. To reduce the amount of data scanned
by Amazon Athena and at the same time improve query speed, what other techniques can you put in place to fulfill this

```
If above statement is for table reservations 

1. Use columnar storage for data storage, as it significantly enhances the speed of data filtering and retrieval.
2. When querying, analysts and data consultants should apply appropriate filters and include the partition column in their queries. 
eg. if the partition is based on checkin_date, it should be specified in the query.
3. Include only the necessary columns in the Sql query
4. When retrieving specific records, use the "LIMIT" clause along with "ORDER BY"
5. Optimize file sizes, aiming for files of at least 1GB, if not 128MB or 256MB, and utilize compression techniques like
 Snappy to store more data in a single file.
6. Use bucketing based on the "reservation_status" column.

```

## Part 2
```
SELECT
  DATE_FORMAT(date, 'YYYY-MM') AS month,
  room_type,
  SUM(booking_amount) AS total_bookings,
  ROUND(AVG(booking_amount), 2) AS average_bookings,
  DENSE_RANK() OVER (PARTITION BY DATE_FORMAT(date, 'YYYY-MM') ORDER BY SUM(booking_amount) DESC) AS rank
FROM
  bookings
GROUP BY
  GROUPING SETS (
    (DATE_FORMAT(date, 'YYYY-MM'), room_type),
    (DATE_FORMAT(date, 'YYYY-MM'))
  )
ORDER BY
  month ASC,
  rank ASC;
```
