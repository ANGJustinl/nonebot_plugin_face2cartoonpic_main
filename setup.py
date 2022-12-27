#!/usr/bin/env python
# coding: utf-8
import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

# Package meta-data.
NAME = 'nonebot_plugin_face2cartoonpic'
DESCRIPTION = '基于 腾讯云合成图的 以图绘图 NoneBot2插件'
URL = 'https://github.com/ANGJustinl/nonebot_plugin_face2cartoonpic'
EMAIL = 'angjustin@163.com'
AUTHOR = 'ANGJustinl'
VERSION = '0.2.5'

setuptools.setup(
    name="nonebot_plugin_face2cartoonpic",
    version="0.2.5",
    author="ANGJustinl",
    author_email="angjustin@163.com",
    keywords=["pip", "nonebot2", "nonebot", "nonebot_plugin"],
    description="""基于 腾讯云合成图的 以图绘图 NoneBot2插件""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ANGJustinl/nonebot_plugin_face2cartoonpic",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    platforms="any",
    install_requires=[
        'nb-cli>=0.6.7'
        'pydantic>=1.9.2'        
    ],
    python_requires=">=3.8"
)
