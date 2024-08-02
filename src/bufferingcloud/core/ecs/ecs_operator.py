from typing import Dict
from datetime import datetime as dt

from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ecs20140526 import models as ecs_20140526_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_console.client import Client as ConsoleClient
from alibabacloud_tea_util.client import Client as UtilClient

from bufferingcloud.base.base_caller import AbstractEcsCaller
from bufferingcloud.utils.account_loader import load_env_variable
from bufferingcloud.core.ecs.exception import EcsGetStateBodyError
from bufferingcloud.core.ecs.exception import EcsStartInstanceBodyError
from bufferingcloud.core.ecs.exception import EcsDescribeInstanceBodyError
from bufferingcloud.core.ecs.exception import EcsDescribeDisksBodyError


class EcsBot(AbstractEcsCaller):
    """
    ECS接口机器人
    """
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
            raise Exception(f"Missing accesskey or secretkey or region,so initlizing the client failed: {e}")

    @classmethod
    def get_state(cls) -> str:
        login_account = load_env_variable()
        ecs_client = cls.initlize_client(login_account)
        if isinstance(login_account, dict):
            describe_instances_status_request = ecs_20140526_models.DescribeInstanceStatusRequest(
                region_id=login_account.get("reg")
            )

        runtime = util_models.RuntimeOptions()
        try:
            ali_ecs_des_instance_resp = ecs_client.describe_instance_status_with_options(describe_instances_status_request, runtime)
            if hasattr(ali_ecs_des_instance_resp, 'body'):
                return UtilClient.to_jsonstring(ali_ecs_des_instance_resp.body)
            else:
                return EcsGetStateBodyError

        except Exception as e:
            raise e

    @classmethod
    async def get_state_async(cls) -> str:
        login_account = load_env_variable()
        ecs_client = cls.initlize_client(login_account)
        if isinstance(login_account, dict):
            describe_instances_status_request = ecs_20140526_models.DescribeInstanceStatusRequest(
                region_id=login_account.get("reg")
            )

        runtime = util_models.RuntimeOptions()
        try:
            ali_ecs_des_instance_resp = await ecs_client.describe_instance_status_with_options(describe_instances_status_request, runtime)
            if hasattr(ali_ecs_des_instance_resp, 'body'):
                return UtilClient.to_jsonstring(ali_ecs_des_instance_resp.body)
            else:
                return EcsGetStateBodyError

        except Exception as error:
            UtilClient.assert_as_string(error.message)

    @classmethod
    def start_single_ecs(cls, pass_instance_id: str) -> str:
        login_account = load_env_variable()
        ecs_client = cls.initlize_client(login_account)
        start_instance_request = ecs_20140526_models.StartInstanceRequest(instance_id=pass_instance_id)
        runtime = util_models.RuntimeOptions()
        try:
            ali_start_ecs_instance_resp = ecs_client.start_instance_with_options(start_instance_request, runtime)
            ConsoleClient.log(UtilClient.to_jsonstring(ali_start_ecs_instance_resp))
            if hasattr(ali_start_ecs_instance_resp, 'body'):
                return UtilClient.to_jsonstring(ali_start_ecs_instance_resp.body)
            else:
                return EcsStartInstanceBodyError

        except Exception as error:
            UtilClient.assert_as_string(error.message)

    @classmethod
    def describe_instances(cls) -> str:
        login_account = load_env_variable()
        ecs_client = cls.initlize_client(login_account)
        if isinstance(login_account, dict):
            describe_instances_request = ecs_20140526_models.DescribeInstancesRequest(
                region_id = login_account.get("reg")
            )
        runtime = util_models.RuntimeOptions()
        try:
            describe_instance_resp = ecs_client.describe_instances_with_options(describe_instances_request, runtime)
            ConsoleClient.log(UtilClient.to_jsonstring(describe_instance_resp))
            if hasattr(describe_instance_resp, 'body'):
                return UtilClient.to_jsonstring(describe_instance_resp.body)
            else:
                return EcsDescribeInstanceBodyError 
        except Exception as error:
            UtilClient.assert_as_string(error.message)

    @classmethod
    async def describe_instances_async(cls) -> str:
        login_account = load_env_variable()
        ecs_client = cls.initlize_client(login_account)
        if isinstance(login_account, dict):
            describe_instances_request = ecs_20140526_models.DescribeInstancesRequest(
                region_id = login_account.get("reg")
            )
        runtime = util_models.RuntimeOptions()
        try:
            describe_instance_resp = await ecs_client.describe_instances_with_options_async(describe_instances_request, runtime)
            if hasattr(describe_instance_resp, 'body'):
                return UtilClient.to_jsonstring(describe_instance_resp.body)
            else:
                return EcsDescribeInstanceBodyError 

        except Exception as error:
            UtilClient.assert_as_string(error.message)

    @classmethod
    async def describe_disks_async(cls, pass_instance_id: str) -> str:
        login_account = load_env_variable()
        ecs_client = cls.initlize_client(login_account)
        if isinstance(login_account, dict):
            describe_disks_request = ecs_20140526_models.DescribeDisksRequest(
                region_id = login_account.get("reg"),
                instance_id = pass_instance_id
            )
        runtime = util_models.RuntimeOptions()
        try:
            describe_disks_resp = await ecs_client.describe_disks_with_options_async(describe_disks_request, runtime)
            if hasattr(describe_disks_resp, 'body'):
                return UtilClient.to_jsonstring(describe_disks_resp.body)
            else:
                return EcsDescribeInstanceBodyError

        except Exception as error:
            UtilClient.assert_as_string(error.message)

    @classmethod
    def create_snapshot(cls, pass_disk_id: str) -> str:
        login_account = load_env_variable()
        ecs_client = cls.initlize_client(login_account)
        create_snapshot_request = ecs_20140526_models.CreateSnapshotRequest(
            disk_id=pass_disk_id,
            snapshot_name=f'backup_before_deploy_{dt.now().strftime("%Y%m%d%H%M%S")}'
        )
        runtime = util_models.RuntimeOptions()
        try:
            create_snapshot_resp = ecs_client.create_snapshot_with_options(create_snapshot_request, runtime)
            if hasattr(create_snapshot_resp, 'body'):
                return UtilClient.to_jsonstring(create_snapshot_resp.body)
            else:
                return EcsDescribeDisksBodyError

        except Exception as error:
            UtilClient.assert_as_string(error.message)

    @classmethod
    async def create_snapshot_async(cls, pass_disk_id: str) -> str:
        login_account = load_env_variable()
        ecs_client = cls.initlize_client(login_account)
        create_snapshot_request = ecs_20140526_models.CreateSnapshotRequest(
            disk_id=pass_disk_id,
            snapshot_name=f'backup_before_deploy_{dt.now().strftime("%Y%m%d%H%M%S")}'
        )
        runtime = util_models.RuntimeOptions()
        try:
            create_snapshot_resp = await ecs_client.create_snapshot_with_options_async(create_snapshot_request, runtime)
            if hasattr(create_snapshot_resp, 'body'):
                return UtilClient.to_jsonstring(create_snapshot_resp.body)
            else:
                return EcsDescribeDisksBodyError

        except Exception as error:
            UtilClient.assert_as_string(error.message)
