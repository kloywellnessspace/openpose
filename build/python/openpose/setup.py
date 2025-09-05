from setuptools import find_packages, setup

setup(
    name="openpose",
    version="1.0.0",
    packages=find_packages(),
    package_data={"openpose": ["*.so", "*.pyd"]},
    include_package_data=True,
)
