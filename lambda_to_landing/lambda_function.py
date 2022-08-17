import json
import boto3
import os

def lambda_handler(event, context):
    result =  json.loads(event["Records"][0]["body"])
    
    pedido=result["Message"]
    
    with open("/tmp/pedido.json","w") as f:
        f.write(pedido)

    bucket_name = os.getenv('BUCKET_NAME')

    s3 = boto3.client('s3')
    s3.upload_file('/tmp/pedido.json', bucket_name, 'input/pedido.json')
    

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
