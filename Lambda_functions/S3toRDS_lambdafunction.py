import json
import boto3
import csv
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import datetime
from io import StringIO

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Print the event for debugging
    print(event)
    
    # Database connection parameters
    connection = mysql.connector.connect(
        host='dg-mysql-inst.c6b0gugiy0nk.us-east-1.rds.amazonaws.com',
        database='industry_db',
        user='admin',
        password='27872268'
    )
    
    # Get bucket and file details from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    csv_file = event['Records'][0]['s3']['object']['key']
    
    # Read the CSV file from S3
    csv_file_obj = s3_client.get_object(Bucket=bucket, Key=csv_file)
    csv_content = csv_file_obj['Body'].read().decode('utf-8')
    
    # Function to preprocess the date
    def preprocess_date(date_str):
        return datetime.strptime(date_str, '%m/%d/%Y %H:%M')
        
    def preprocess_date1(date_str):
        return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    
    # Determine the appropriate SQL query based on the file name
    if "PdM_machines" in csv_file:
        query = 'INSERT INTO machines_tbl(machineID, model, age) VALUES (%s, %s, %s)'
        data = []
        for row in csv.DictReader(StringIO(csv_content)):
            data.append((row['machineID'], row['model'], row['age']))
    
    elif "PdM_failures" in csv_file:
        query = "INSERT INTO failures_tbl (datetime, machineID, failure) VALUES(%s, %s, %s)"
        data = []
        for row in csv.DictReader(StringIO(csv_content)):
            processed_date = preprocess_date1(row['datetime'])
            data.append((processed_date, row['machineID'], row['failure']))
    
    elif "PdM_errors" in csv_file:
        query = "INSERT INTO errors_tbl (datetime, machineID, errorID) VALUES(%s, %s, %s)"
        data = []
        for row in csv.DictReader(StringIO(csv_content)):
            processed_date = preprocess_date1(row['datetime'])
            data.append((processed_date, row['machineID'], row['errorID']))
    
    elif "PdM_maint" in csv_file:
        query = "INSERT INTO maintainances_tbl (datetime, machineID, comp) VALUES(%s, %s, %s)"
        data = []
        for row in csv.DictReader(StringIO(csv_content)):
            processed_date = preprocess_date1(row['datetime'])
            data.append((processed_date, row['machineID'], row['comp']))
        
    elif "PdM_telemetry" in csv_file:
        query = "INSERT INTO telemetry_tbl (datetime, machineID, volt, rotate, pressure, vibration) VALUES(%s, %s, %s, %s, %s, %s)"
        data = []
        for row in csv.DictReader(StringIO(csv_content)):
            processed_date = preprocess_date1(row['datetime'])
            data.append((processed_date, row['machineID'], row['volt'], row['rotate'], row['pressure'], row['vibration']))
    
    # Insert data into the database
    cursor = connection.cursor()
    cursor.executemany(query, data)
    
    # Commit the transaction
    connection.commit()
    
    # Print the number of records inserted
    print(cursor.rowcount, 'Record inserted successfully into industry_data table')
    
    # Close the cursor and connection
    cursor.close()
    connection.close()
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
