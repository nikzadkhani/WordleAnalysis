#
# setup.py
#
# creates wordle package
#

from setuptools import find_packages, setup

TEST_REQUIREMENTS = ["pytest~=7.0.1", "black~=22.1.0", "flake8~=4.0.1"]

setup(
    name="wordle",
    description="A package for playing and analyzing games of wordle.",
    author="Nikzad Khani, Rishab Nayak",
    author_email="khaninikzad@gmail.com",
    packages=find_packages(),
    extras_require={"test": TEST_REQUIREMENTS},
)
