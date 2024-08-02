import os
from typing import List,Generator

__all__ = [
    "find_keyfile",
    "print_helloworld"
]


class FastFinder:
    # @classmethod
    # def files_find(cls, start_path: str) -> Generator[str, None, None]:
    #     """
    #     param: start_path type string 
    #     must be abs path
    #     return generator yielding file paths
    #     """
    #     if os.path.isfile(start_path):
    #         yield start_path

    #     if os.path.isdir(start_path):
    #         for files in os.listdir(start_path):
    #             abs_path = os.path.join(start_path, files)
    #             if os.path.isfile(abs_path):
    #                 yield abs_path

    #             if os.path.isdir(abs_path):
    #                 yield from cls.files_find(abs_path)
    
    # @classmethod
    # def files_find(cls, start_path: str) -> List[str]:
    #     """
    #     param: start_path type string 
    #     must be abs path
    #     return file list
    #     """
    #     file_list = []
    #     if os.path.isfile(start_path):
    #         return [start_path]

    #     if os.path.isdir(start_path):
    #         for files in os.listdir(start_path):
    #             abs_path = os.path.join(start_path, files)
    #             if os.path.isfile(abs_path):
    #                 file_list.append(abs_path)

    #             if os.path.isdir(abs_path):
    #                 file_list.extend(cls.files_find(abs_path))

    #     return file_list

    
    @classmethod
    def files_find(cls, key_file: str,start_path: str) -> Generator[str]:
        """
        param: start_path type string 
        must be abs path
        return file list
        """
        # TODO : 
        # 1. 递归遍历文件夹
        # 2. 遍历文件夹，判断文件名是否包含key_file
        
        dir_lis = list()
        file_lis = list()
        if os.path.isfile(start_path):
            return [start_path]
        
        if os.path.isdir(start_path):
            dir_lis.append(start_path)
            list_dir = os.listdir(start_path)

            for files in list_dir:
                abs_path = os.path.join(start_path, files)
                if os.path.isfile(abs_path):
                    file_lis.append(abs_path)

                if os.path.isdir(abs_path):
                    dir_lis.append(abs_path)
                    yield abs_path
                    cls.files_find(abs_path)

        return file_lis
    
    @classmethod
    def hello_world(cls, counter: int) -> None:
        count_time = 1
        if isinstance(counter, int):
            while counter:
                if counter and counter > 0:
                    print(f"第{count_time}🗡 Hello world...")
                    count_time += 1
                    counter -= 1
                    
                if counter and counter < 0: 
                    # counter = abs(counter)
                    print(f"第{count_time}🗡 Hello world...")
                    count_time += 1
                    counter += 1

find_keyfile = FastFinder.files_find
print_helloworld = FastFinder.hello_world

# class TestMonkeyPatch:
#     def 