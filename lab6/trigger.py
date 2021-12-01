import boto3
import json
import urllib.parse



def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_output = 'bucket2-oscarteeninga'
    file_name = 'oteeninga_sample.txt'
    
    try:
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

        response = s3.get_object(Bucket=bucket, Key=key)
        file = response['Body'].read().decode('utf-8')
        print("File: " + str(file))
        file_extended = (str(file) + ' by s3').encode('ascii')
        s3.put_object(Body=file_extended, Bucket=bucket_output, Key=file_name + 'copy')
        # TODO implement
        return {
            'statusCode': 200,
            'body': json.dumps(response['ContentType'])
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body':  json.dumps(str(e))
        }


