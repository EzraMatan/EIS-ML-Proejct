from setuptools import setup, find_packages

setup(
    name = "yourpackage",
    version = "1.2.0",
    description = "Simple description",
    packages = find_packages(),
    install_requires = ['matplotlib']  # Example of external package
)