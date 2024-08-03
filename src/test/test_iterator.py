import os
import inspect
from file_find import find_keyfile, print_helloworld


# 方法一: 获取当前执行环境的文件路径
current_file = inspect.getfile(inspect.currentframe())
here = os.path.dirname(os.path.abspath(current_file))
here = "/home/python/code-repo/cloud-sdk/src/"
print(f"Sloution first:--> {here}")

# 方法二: 获取当前执行环境的文件路径
current_path = os.getcwd()
print(f"Sloution second:--> {current_path}")


# 启动函数
def test_run_file_finder(want_file: list,
                    start_path: str) -> None:
    
    result_file_lis = find_keyfile(start_path)
    print(result_file_lis)
    
    # 这里有问题
    # if [os.path.basename(x) for x in result_file_lis if x in want_file]:
    #     print([os.path.basename(x) for x in result_file_lis if x in want_file])


print_helloworld(10)
target_file_name = ["runner.py"]
test_run_file_finder(want_file = target_file_name, start_path = here)