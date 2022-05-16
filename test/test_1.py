import os
from app import test
import pathlib
def test_1():
    mocka=2
    mockb=3
    obj=test()
    assert obj.sum1(mocka,mockb)==5

import boto3
from moto import mock_s3

BUCKET_NAME = "mybucket"
FILE_NAME = "red.jpg"
FILE_LOCATION = FILE_NAME
import os
import pytest

try:
    from temp_env_var import TEMP_ENV_VARS
except ImportError:
    print("error")
    TEMP_ENV_VARS = {}
    ENV_VARS_TO_SUSPEND = []
@mock_s3
def test_aws() -> None:
     
     parent_dir = pathlib.Path(__file__).resolve().parent.parent
     print(parent_dir)
     print(os.path.join(parent_dir,'red.jpg' )  )
     print("hello",os.environ["AWS_DEFAULT_REGION"])
     from app import test,ObjectStorage
     obj_aws=ObjectStorage()
     
     assert isinstance(obj_aws,ObjectStorage)
    
  
     assert obj_aws.image==None

     s3 = boto3.resource("s3")
     bucket = s3.create_bucket(Bucket=BUCKET_NAME)
     s3 = boto3.client('s3')

     with open(FILE_LOCATION, 'rb') as data:
        s3.upload_fileobj(data, BUCKET_NAME, FILE_NAME)
parent_dir = pathlib.Path(__file__).resolve().parent.parent
print(parent_dir)
print(os.path.join(parent_dir,'red.jpg' )  )
# @mock_s3
# def test_check_image():
     
#      obj_aws=ObjectStorage()

#      responce,failed=obj_aws.check_image(bucket=BUCKET_NAME,key=FILE_NAME)
#      assert failed==True    
