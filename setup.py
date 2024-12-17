from pathlib import Path

import setuptools
from pkg_resources import parse_requirements

import python_dependency_resolver

with open("README.md", "r") as fh:
    long_description = fh.read()

path = Path("requirements.txt")
install_requires = [str(ir) for ir in parse_requirements(path.open())]

setuptools.setup(
    name="python-dependency-resolver",
    version=python_dependency_resolver.get_version(),
    author="Anthony K GROSS",
    author_email="anthony.k.gross@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://anthonykgross.fr/python-dependency-resolver/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    include_package_data=True,
    install_requires=install_requires,
    project_urls={
        'Documentation': 'https://anthonykgross.fr/python-dependency-resolver/',
        'Source': 'https://github.com/anthonykgross/python-dependency-resolver/',
    }
)
