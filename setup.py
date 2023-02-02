"""Setup the database package..."""

from setuptools import find_packages, setup

setup(
    name="kalender",
    version="0.9.0",
    author="Simon Retter",
    author_email="retter190085@sr.htlweiz.at",
    description="Kalender app",
    url="https://upstream",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6',
)
