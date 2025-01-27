from setuptools import setup, find_packages

setup(
    name="WikiApi",
    version="0.0.1",
    author="ali",
    author_email="liaraeesi@gmail.com",
    description="APIs of a telegram channel that's in the hands of Iranians, which is relatively good.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/aliraeesi385/WikiApi",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.14",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: Persian",
    ],
    python_requires='>=3.14',
    install_requires=[
        "requests",
    ],
)
