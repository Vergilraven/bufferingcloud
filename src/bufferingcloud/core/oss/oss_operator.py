import oss2
from oss2.credentials import EnvironmentVariableCredentialsProvider
from oss2.models import BucketLogging


class OssBot:

    @classmethod
    def enable_logging(region_id: str) -> callable:
        auth = oss2.ProviderAuth(EnvironmentVariableCredentialsProvider())  
        bucket = oss2.Bucket(auth, f'https://oss-{region_id}.aliyuncs.com', 'examplebucket')
        logging = bucket.put_bucket_logging(BucketLogging(bucket.bucket_name, 'log/'))
        if logging.status == 200:
            print("Enable access logging")
        else:
            print("request_id:", logging.request_id)
            print("resp:", logging.resp.response)

