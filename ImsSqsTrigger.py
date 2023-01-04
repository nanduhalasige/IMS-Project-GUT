import json
import boto3

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    record = event['Records'][0]['body']
    rows = record.split('\n')
    
    table = dynamodb.Table('ims_data_new')
    
    with table.batch_writer() as batch:
        for row in rows:
          
            batch.put_item(Item={
                'identyfikator': row.split(',')[0],
                'lokalizacja': row.split(',')[1],
                'x': row.split(',')[2],
                'y': row.split(',')[3]
            })
