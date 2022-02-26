#
# setup.py
#
# creates wordle package
#
# TODO: add tests

from setuptools import find_packages, setup

setup(
    name="wordle",
    description="A package for playing and analyzing games of wordle.",
    author="Nikzad Khani, Rishab Nayak",
    author_email="khaninikzad@gmail.com",
    packages=find_packages(),
)
