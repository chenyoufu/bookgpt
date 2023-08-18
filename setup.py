#!/usr/bin/env python3
from setuptools import find_packages, setup

packages = [
    "bs4",
    "openai",
    "litellm",
    "requests",
    "ebooklib",
    "rich",
    "tqdm",
    "tiktoken",
    "PyDeepLX",
]

setup(
    name="bookgpt",
    description="",
    version="1.0",
    license="MIT",
    author="youfu",
    author_email="youfu.ok@163.com",
    packages=find_packages(),
    url="https://github.com/chenyoufu/bookgpt",
    python_requires=">=3.8",
    install_requires=packages,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
