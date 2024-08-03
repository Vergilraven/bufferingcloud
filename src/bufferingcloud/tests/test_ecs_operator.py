import pytest

from typing import Dict
from bufferingcloud.core.api import get_ecs_status
from bufferingcloud.core.api import sync_get_ecs_status
from bufferingcloud.core.api import sync_describe_disks
from bufferingcloud.core.api import sync_create_ecs_snapshot
from bufferingcloud.core.api import start_single_ecs
from .test_account_loader import generate_account_configuration
from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_tea_openapi import models as open_api_models


class TestEcsBot:

    @staticmethod
    def initlize_client(pass_sensitive_data: Dict[str, str]) -> Ecs20140526Client:
        """
        TODO: STStoken的方式初始化
        使用AK&SK初始化账号Client
        @return: Client
        @throws Exception
        """
        try:
            config = open_api_models.Config(
                access_key_id=pass_sensitive_data["ak"],
                access_key_secret=pass_sensitive_data["sk"]
            )

            config.endpoint = f'ecs.{pass_sensitive_data["reg"]}.aliyuncs.com'
            return Ecs20140526Client(config)

        except KeyError as e:
            raise Exception(f"AccessKey,Secretkey,region are missed,So that initlize the client failed: {e}")

def test_init_client():
    access_key = generate_account_configuration(2)[0]
    secret_key = generate_account_configuration(2)[1]
    region_id = "cn-shenzhen"
    
    ecs_client = TestEcsBot.initlize_client()

def test_get_ecs_status():
    current_ecs_status = get_ecs_status
    assert type(current_ecs_status) == str
    assert current_ecs_status == "Running"
