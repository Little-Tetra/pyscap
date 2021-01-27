import re

from setuptools import setup, find_packages


def get_version():
    with open("pyscap/__init__.py", encoding="utf8") as f:
        return re.search(r'__version__ = "(.*?)"', f.read()).group(1)


setup(
    name='pyscap',
    version=get_version(),
    packages=find_packages(),
    url='https://github.com/Little-Tetra/pyscap',
    license='MIT',
    author='Kevin Ju',
    description='Python package for handling Security Content Automation Protocol.',
    install_requires=[
        "xsdata"
    ]
)
