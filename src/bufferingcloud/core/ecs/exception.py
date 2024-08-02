class EcsGetStateBodyError(ValueError):
    """Something error happend while calling Get Ecs Status API"""


class EcsStartInstanceBodyError(ValueError):
    """Something error happend while calling start instance API"""


class EcsDescribeInstanceBodyError(ValueError):
    """Something error happend while calling describe instance API"""


class EcsDescribeDisksBodyError(ValueError):
    """Something error happend while calling describe disks API"""
