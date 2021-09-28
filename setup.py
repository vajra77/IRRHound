from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="irrhound",
    version="0.1",
    author="Francesco Ferreri",
    author_email="f.ferreri@namex.it",
    description="A package to check for IRR resources",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/vajra77/IRRHound",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: CC0 1.0 Universal",
    ],
)
