import os 

# here = os.path.abspath(os.path.dirname(__file__))
# second_here = os.getcwd()


# def test_walk():
#     for root, dirs, files in os.walk(here):
#         print(root)
#         print(dirs[:])
#         print(files)


# test_walk()

import os
import unittest
from setuptools import find_packages

class TestPackageFinder(unittest.TestCase):    

    def setUp(self):
        self.test_dir = 'test_dir'
        os.makedirs(self.test_dir, exist_ok = True) # 创建 mkdir 目录 形式参数 exist_ok 实际参数 布尔值boolean True
        self.where = os.path.join(self.test_dir, 'valid_package')
        os.makedirs(self.where, exist_ok = True)
        with open(os.path.join(self.where, '__init__.py'), 'w') as f:
            f.write('')

        # 创建一个子包
        self.subpackage = os.path.join(self.where, 'subpackage')
        os.makedirs(self.subpackage, exist_ok=True)
        with open(os.path.join(self.subpackage, '__init__.py'), 'w') as f:
            f.write('')

        # 创建一个非包目录
        os.makedirs(os.path.join(self.test_dir, 'not_a_package'), exist_ok=True)

    def tearDown(self):
        # 清理测试环境
        os.remove(os.path.join(self.where, '__init__.py'))
        os.rmdir(self.subpackage)
        os.rmdir(self.where)
        os.rmdir(os.path.join(self.test_dir, 'not_a_package'))
        os.rmdir(self.test_dir)

    def test_find_packages_iter_includes_all(self):
        # 测试包括所有包的情况

        def include(package):
            return True

        def exclude(package):
            return False

        expected_packages = ['valid_package', 'valid_package.subpackage']
        packages = list(find_packages(self.test_dir, exclude, include))

        self.assertEqual(expected_packages, packages)


    def test_find_packages_iter_excludes_none(self):
        # 测试不排除任何包的情况

        def include(package):
            return True

        def exclude(package):
            return True  # Excludes nothing as the condition is always false.

        expected_packages = ['valid_package', 'valid_package.subpackage']
        packages = list(find_packages(self.test_dir, exclude, include))

        self.assertEqual(expected_packages, packages)

    def test_find_packages_iter_excludes_some(self):
        # 测试排除部分包的情况

        def include(package):
            return 'subpackage' not in package

        def exclude(package):
            return False

        expected_packages = ['valid_package']
        packages = list(find_packages(self.test_dir, exclude, include))

        self.assertEqual(expected_packages, packages)


if __name__ == '__main__':
    unittest.main()