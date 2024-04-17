from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="tc-core-analyzer-lib",
    version="1.3.0",
    author="Mohammad Amin Dadgar, TogetherCrew",
    maintainer="Mohammad Amin Dadgar",
    maintainer_email="dadgaramin96@gmail.com",
    packages=find_packages(),
    description="TogetherCrew core analyzer library.",
    long_description=open("README.md").read(),
    install_requires=requirements,
)
