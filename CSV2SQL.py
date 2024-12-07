
# The idea is to insert the data into a sql table

import csv
import psycopg2

# Connect to PostgreSQL database
# Database connection parameters
db_params = {
    'dbname': 'work',
    'user': 'postgres',
    'password': 'letme2G@tin',
    'host': 'localhost',  # Or your server address
    'port': 5432          # Default PostgreSQL port
}

# Connect to PostgreSQL
try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Open the CSV file
    with open('C:/Users/USUARIO/projects/python/portfolio/work/data/TDESC04.csv', 'r') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)  # Skip the header row

        # Insert each row into the PostgreSQL table
        for row in csv_reader:
            cursor.execute(
                "INSERT INTO tdesc04 (country, job, param, aval, parameter) VALUES (%s, %s, %s, %s, %s)",
                row
            )

    # Commit the transaction
    conn.commit()


    print("Data successfully inserted into the PostgreSQL table.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the database connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()












