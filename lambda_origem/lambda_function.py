import json
import boto3

def lambda_handler(event, context):
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    path_file = event["Records"][0]["s3"]["object"]["key"].replace('%2F', '/')
    
    path_file_tmp = '/tmp/meuarquivo.json'
    
    s3 = boto3.resource('s3')
    s3.meta.client.download_file(bucket_name, path_file, path_file_tmp)
    
    file_json = open(path_file_tmp)
    meu_pedido = json.load(file_json)
    file_json.close()
    
    sns = boto3.client('sns')

    response = sns.publish(
        TopicArn='arn:aws:sns:us-east-1:ID_ACCOUNT:NOME_TOPIC_SNS',
        Message=json.dumps(meu_pedido)

    )

    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
