from abc import ABC, abstractmethod
from alibabacloud_ecs20140526.client import Client as Ecs20140526Client


class AbstractEcsCaller(ABC):

    # 封装了一系列的接口调用业务逻辑形成自动化云基础设施管理
    @abstractmethod
    def initlize_client() -> Ecs20140526Client:
        pass

    @abstractmethod
    def get_state(cls, ecs_client: Ecs20140526Client) -> str:
        pass

    @abstractmethod
    async def get_state_async(cls) -> str:
        pass

    @abstractmethod
    async def start_single_ecs(cls, pass_instance_id: str) -> str:
        pass

    @abstractmethod
    async def describe_instances_async(cls) -> str:
        pass

    @abstractmethod
    async def describe_disk_async(cls, pass_instance_id: str) -> str:
        pass

    @abstractmethod
    async def create_snapshot_async(cls, pass_disk_id: str) -> str:
        pass
