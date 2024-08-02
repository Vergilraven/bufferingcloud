from bufferingcloud.core.ecs.ecs_operator import EcsBot


"""
1. 获取ECS状态
2. 启动ECS
3. 异步获取ECS状态
4. 异步描述云盘信息
5. 异步创建快照
"""

get_ecs_status = EcsBot.get_state
start_single_ecs = EcsBot.start_single_ecs
sync_get_ecs_status = EcsBot.get_state_async
sync_describe_instances = EcsBot.describe_instances_async
sync_describe_disks = EcsBot.describe_disks_async
sync_create_ecs_snapshot = EcsBot.create_snapshot_async

__all__ = ["get_ecs_status",
           "sync_get_ecs_status",
           "start_single_ecs",
           "sync_get_ecs_status",
           "sync_describe_disks",
           "sync_create_ecs_snapshot"]
