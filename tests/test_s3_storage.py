import unittest
from media.s3_storage import S3MediaStorage 
import boto3
import os

class TestS3Storage(unittest.TestCase):

  def test_it_allow_store_media_from_path(self):
    #A arrange
    self.there_is_source_file("files/test.txt")
    s3 = self.there_is_s3_resource_available()
    storage = S3MediaStorage(s3, os.getenv('APP_BUCKET_NAME'))

    #A act
    to_be_upl = open("files/test.txt", 'rb')
    storage.store(dest="tests/foo/boo.txt", source=to_be_upl)

    #A assert
    assert storage.contains(path="tests/foo/boo.txt")
    assert False == storage.contains(path="should/not/exists.txt")

  def there_is_source_file(self, path):
    my_file = open(path, 'w')
    my_file.write("content of test file")
    my_file.close()
  
  def there_is_s3_resource_available(self):
    return boto3.resource('s3')
if __name__ == '__main__':
    unittest.main()
