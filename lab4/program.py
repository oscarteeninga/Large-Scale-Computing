
import requests
import time
import boto3

ec2_client = boto3.client('ec2')
instance_id = 'i-0a9998aee64126560'

start_t = time.time()

res = ec2_client.start_instances(InstanceIds=[instance_id])
print(res)

while res != 'running':
    time.sleep(0.1)
    res_call = ec2_client.describe_instances(InstanceIds=[instance_id])
    instance = res_call['Reservations'][0]['Instances'][0]
    res = instance['State']['Name']
    print(res)
    
print(res)
print("Start time:", time.time() - start_t, "s")

ip = instance['PublicDnsName']
print("IP Address:", ip)
f = requests.get('http://' + ip, allow_redirects=True)
print(f.content)

stop = ec2_client.stop_instances(InstanceIds=[instance_id])
print(stop)

