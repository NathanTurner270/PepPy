import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "PepPy",
    version = "1.0.0",
    author = "Nate Turner",
    author_email = "nathanturner270@gmail.com",
    description = ("This package will ease your Peplink pains. You will no longer suffer with the 'built-in' Peplink API that never fully works. It's as easy to use as one function call."),
    url = "https://github.com/NathanTurner270/PepPy",
    packages=find_packages(include=['PepPy', 'PepPy.*']),
    long_description=read('README.md'),
    install_requires=[
        "requests",
        "httpretty",
        'urllib3',
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
)