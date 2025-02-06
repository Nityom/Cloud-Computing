# import boto3

# # Initialize S3 client
# s3 = boto3.client("s3")

# # List S3 buckets
# response = s3.list_buckets()
# print("S3 Buckets:", [bucket["Name"] for bucket in response["Buckets"]])


import boto3

# Initialize S3 client
s3_client = boto3.client("s3")

def list_s3_objects(bucket_name):
    response = s3_client.list_objects_v2(Bucket=bucket_name)

    if "Contents" in response:
        for obj in response["Contents"]:
            print(f"File Key: {obj['Key']}")  # Print file key
    else:
        print("No files found in the bucket.")

# Replace with your bucket name
bucket_name = "nityombaalti"
list_s3_objects(bucket_name)
