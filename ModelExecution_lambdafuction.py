import json
import boto3
import psycopg2
import os
import pandas as pd
from io import StringIO

# Initialize SageMaker runtime client
sagemaker_runtime = boto3.client('sagemaker-runtime')

# Environment variables (set in Lambda console)
ENDPOINT_NAME = os.environ['RF_endpoint']

def lambda_handler(event, context):
    # Get bucket and file details from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    csv_file = event['Records'][0]['s3']['object']['key']

    # Read the CSV file from S3
    csv_file_obj = s3_client.get_object(Bucket=bucket, Key=csv_file)
    csv_content = csv_file_obj['Body'].read().decode('utf-8')

    query = 'INSERT INTO test_tbl(machineID, age, volt, rotate, pressure, vibration, comp1_cnt, comp2_cnt, comp3_cnt, comp4_cnt, error1_cnt, error2_cnt, error3_cnt, error4_cnt, error5_cnt, model_model1, model_model2, model_model3, model_model4) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    data = []
    for row in csv.DictReader(StringIO(csv_content)):
        data.append((row['machineID'], row['age'], row['volt'], row['rotate'], row['pressure'], row['vibration'], row['comp1_cnt'], row['comp2_cnt'], row['comp3_cnt'], row['comp4_cnt'], row['error1_cnt'], row['error2_cnt'], row['error3_cnt'], row['error4_cnt'], row['error5_cnt'], row['model_model1'], row['model_model2'], row['model_model3'], row['model_model4']))
    df = pd.DataFrame(data)

    # Send request to SageMaker endpoint
    response = sagemaker_runtime.invoke_endpoint(
        EndpointName=ENDPOINT_NAME,
        ContentType='application/json',
        Body=df.iloc[1:].to_json(orient='records')
    )

    result = response['Body'].read().decode('utf-8')
    predictions = json.loads(result)

    # Merge predictions with input data
    df['failure1_prob','failure2_prob','failure3_prob','failure4_prob'] = predictions
    df['predicted_class'] = [p.index(max(p)) for p in predictions]  # Predicted class index

    # Insert into RDS
    conn = mysql.connector.connect(
    host='dg-mysql-inst.c6b0gugiy0nk.us-east-1.rds.amazonaws.com',
    database='industry_db',
    user='admin',
    password='27872268'
    )
    cur = conn.cursor()

    # Insert row by row (can be optimized via batch insert)
    for _, row in df.iterrows():
        columns = ','.join(row.index)
        values = ','.join(['%s'] * len(row))
        insert_stmt = f"INSERT INTO prediction_results ({columns}) VALUES ({values})"
        cur.execute(insert_stmt, tuple(row.values))

    conn.commit()
    cur.close()
    conn.close()

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Predictions stored successfully', 'predictions': predictions})
    }
