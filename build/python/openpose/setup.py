from setuptools import setup, find_packages
import os

setup(
    name="openpose",
    version="1.0",
    packages=find_packages(),
    package_data={
        "openpose": ["*.so"],  # Include the compiled shared object
    },
    include_package_data=True,
    description="Python API for OpenPose",
    author="CMU Perceptual Computing Lab",
    url="https://github.com/CMU-Perceptual-Computing-Lab/openpose",
)
