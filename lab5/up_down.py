import time
import boto3
import botocore

file_name = 'plik'
bucket_name = 'bucket-oscarteeninga'

start_time = time.time()

s3 = boto3.resource('s3')

file = s3.Object(bucket_name, file_name)

result = file.put(Body=open(file_name, 'rb'))

response = result.get('ResponseMetadata')

print("Upload time: " + str(time.time() - start_time))

start_time = time.time()
if response.get('HTTPStatusCode') != 200:
    print("File not upload")
else:
    print("File uploaded")
    
try:
    s3.Bucket(bucket_name).download_file(file_name, file_name)
except e:
    print(e)
    
print("Download time: " + str(time.time() - start_time))
    

