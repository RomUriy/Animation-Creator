import botocore

class S3MediaStorage:
 
  def __init__(self, s3, bucket_name):
    self.s3 = s3
    self.bucket_name = bucket_name
    self.bucket = s3.Bucket(bucket_name)

  def store(self, dest, source):
    self.bucket.put_object(Key=dest, Body=source)

  def contains(self, path):
    try:
      self.s3.Object(self.bucket_name, path).load()
      return True
    except botocore.exceptions.ClientError as e:
      return False
