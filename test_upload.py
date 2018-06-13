import boto3

bucket_name = ''
s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)

my_file = open('my_hello.txt', 'rb')
bucket.put_object(Key='omega/gamma/alfa/hello.txt', Body=my_file)

