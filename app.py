import boto3

class test():
 def sum1(self,a,b):
      return a+b
from moto import mock_s3
# @mock_s3
class ObjectStorage:
    def __init__(self) -> None:
       
        from utils.config import AWS_DEFAULT_REGION

        # Create boto3 Session for making boto3 calls.
        session = boto3.Session(region_name=AWS_DEFAULT_REGION)
        self.client = session.client("s3")

        self.image = None