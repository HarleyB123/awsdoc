from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="awsdocs",
    version="0.0.7",
    author="Harley Bates",
    author_email="HarleyBatesOfficial@yahoo.co.uk",
    description="Opens AWS Developer guide for a given AWS service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HarleyB123/awsdoc",
    packages=find_packages(include=['src', 'src.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": ["awsdocs = src.awsdocs:main",],},
    python_requires=">=3.6",
)
