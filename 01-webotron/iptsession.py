# coding: utf-8
import boto3

session = boto3.Session(profile_name='pythonAutomation')
session.available_profiles
s3 = session.resource('s3')

for bucket in s3.buckets.all():
    print(bucket)
    
#new_bucket = s3.create_bucket(Bucket='automating-aws-moh')    
ec2_client = session.client('ec2','us-east-1')
