"""
MIT License

Copyright (c) 2024 Vergil

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import codecs
import importlib.util
from setuptools import setup, find_packages


"""
bufferingcloud client
copy from alibabacloud_sample.
Created on 18/06/2024
@maintainer: VergilHe
@email: 691267837@qq.com
"""
here = os.path.abspath(os.path.dirname(__file__))
spec = importlib.util.spec_from_file_location("bufferingcloud", "src/bufferingcloud/__init__.py")
bufferingcloud = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bufferingcloud)

PACKAGE = "src/bufferingcloud"
NAME = "bufferingcloud" or "bufferingcloud-integration"
DESCRIPTION = "BufferingCloud Client integration of Alicloud Python3 sdk"
AUTHOR = "VergilHe"
AUTHOR_EMAIL = "vergilheyeahfun@gmail.com"
URL = "https://github.com/VergilRaven/bufferingcloud"
VERSION = bufferingcloud.__version__
REQUIRES = [
    "alibabacloud-credentials==0.3.2",
    "alibabacloud-ecs20140526==3.0.8",
    "alibabacloud-endpoint-util==0.0.3",
    "alibabacloud-gateway-spi==0.0.1",
    "alibabacloud-openapi-util==0.2.1",
    "alibabacloud-rds20140815==2.1.4",
    "alibabacloud-tea==0.3.2",
    "alibabacloud-tea-console==0.0.1",
    "alibabacloud-tea-openapi==0.3.7",
    "alibabacloud-tea-util==0.3.8",
    "alibabacloud-tea-xml==0.0.2",
    "aliyun-python-sdk-core==2.13.36",
    "aliyun-python-sdk-ecs==4.24.64",
    "aliyun-python-sdk-kms==2.16.3",
    "aliyun-python-sdk-rds==2.7.19",
    "oss2==2.18.6",
    "PyYAML==6.0.1"
]

LONG_DESCRIPTION = 'Intergrate the alibabacloud python3 sdk'
if os.path.exists('README.md'):
    with codecs.open(filename=os.path.join(here, "README.md"), encoding="utf-8") as fh:
        LONG_DESCRIPTION = "\n" + fh.read()


setup(
    name=NAME,
    version="0.0.1",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="MIT",
    url=URL,
    keywords=["bufferingcloud", "intergrate alibaba-cloud python3 sdk"],
    packages=find_packages(where="src", exclude=["tests*"],
                           include=["bufferingcloud"]),
    include_package_data=True,
    platforms="any",
    package_dir={"": "src"},
    install_requires=REQUIRES,
    python_requires=">=3.6",
    classifiers=(
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Topic :: Intergrate Alibaba-cloud python3 sdk"
    )
)
