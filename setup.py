from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ['ipwhois>=1.2.0']

setup(
    name="irrhound",
    version="1.2.2",
    author="Francesco Ferreri",
    author_email="f.ferreri@namex.it",
    description="A package to check for IRR resources",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/vajra77/IRRHound",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',  # Define that your audience are developers
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Programming Language :: Python :: 3.8"
    ],
)
