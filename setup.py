from setuptools import setup, find_packages

setup(
    name="pyRM",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pyhere>=1.0.0"      # specify the minimum version if needed
    ],
)