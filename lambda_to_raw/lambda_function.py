import json
import pandas as pd
import boto3


def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_path = event['Records'][0]['s3']['object']['key'].replace('%2F', '/')
    s3 = boto3.resource('s3')
    s3.meta.client.download_file(bucket_name, file_path, '/tmp/pedido.json')
    df = pd.read_json('/tmp/pedido.json')
    df.to_parquet('/tmp/pedido.parquet')
    bucket_name_target = os.getenv('BUCKET_NAME_TARGET')  
    s3 = boto3.client('s3')
    with open('/tmp/pedido.parquet', 'rb') as data:
        s3.upload_fileobj(data, bucket_name_target, 'pedido.parquet')
        
    return 200
