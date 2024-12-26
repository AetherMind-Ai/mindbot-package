from setuptools import setup, find_packages

setup(
    name='mindbotai',
    version='0.1.0',  # Change as needed
    packages=find_packages(),
    install_requires=[
        'google-generativeai',  # Add any other dependencies
    ],
)