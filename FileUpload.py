import json
import base64
import boto3

sqs = boto3.client('sqs')
queue_url = 'https://sqs.us-east-1.amazonaws.com/832286995734/IMSQueue'


def lambda_handler(event, context):
    file_content = base64.b64decode(event['body-json']).decode('utf-8').split('\n')
    print(file_content)
    csvData = file_content[1:len(file_content)]
    csvString = '\n'.join(csvData) 
    print('i am alive')
    print(csvString)
    response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody=(
        csvString.replace('\r', '')
        )
    )
    
    return response
   

    # print(response['MessageId'])