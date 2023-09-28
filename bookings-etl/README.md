# Prerequisites
1. Spark==2.4.5
2. Python=3.8.0
3. Pyspark==3.0.0
4. py4j==0.10.9
5. pypandoc==1.11

# How to run program files
1. Clone or download this project to your local machine.
2. Open a terminal and navigate to the project directory.
3. Ensure you have Apache Spark installed and properly configured.
4. Make sure you have the PySpark library installed. If not, you can install it using pip: `pip install pyspark`
5. Open your IDE and simply run the `main_app.py` file 
6. This command submits the Spark application, and it will execute all the transformation of the ETL process using
the `transformations.py` module.
7. Once the application has finished running, you can find the Parquet output in the output directory /ETL-output.
8. Run the unit tests in tests/test_transformation.

# Directory Structure 

```
-- ETL-input
    |
     -- input_data.csv
-- ETL-output
    |
     -- output_data
-- src
    |
     -- __init__.py
    |
     -- main_app.py
    |
     -- transformations.py
-- tests
    |
     -- test_data.py
    |
     -- test_transformations.py
-- __init__.py
-- README.md

```