'''
	You must replace <FMI> with your bucket name
'''
import boto3
import json

S3API = boto3.client("s3", region_name="us-west-2") 
bucket_name = "lab-01-s3site"

policy_file = open("bucket-policy.json", "r")


S3API.put_bucket_policy(
    Bucket = bucket_name,
    Policy = policy_file.read()
)
print ("DONE")