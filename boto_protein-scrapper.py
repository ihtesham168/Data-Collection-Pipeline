import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('protein-scrapper')
for file in bucket.objects.all():
    print(file.key)
    