import pathlib
from setuptools import setup # type: ignore

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

f = open("./VERSION", "r")
version = f.read()

# This call to setup() does all the work
setup(
    name="pyshopify",
    version=version,
    description="An alternative wrapper for the Shopify API",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/lowercase00/pyshopify",
    author="Lowercase",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["reader"],
    include_package_data=True,
    install_requires=["requests", "pydantic"],
    entry_points={
        "console_scripts": [
            "realpython=reader.__main__:main",
        ]
    }
)