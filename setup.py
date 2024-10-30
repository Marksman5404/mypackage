from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='1.0',
    packages=find_packages(exclude=['tests*']),
    licence='MIT',
    description='EDSA example python package',
    long_description=('README.md'),
    install_requires=['numpy'],
    url='https://github.com/marksman5404/package-name',
    author='Your Name',
    author_email='akinyemido@gmail',

)
