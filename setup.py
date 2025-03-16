from setuptools import setup, find_packages

setup(
    name = "cars",
    version = "1.0",
    author = "Dinusha Senartahna",
    author_email = "",
    url = "",
    description = "",
    pakages = find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = ["numpy", "matplotlib.pyplot"],
    entry_points = {"console_scripts" : ["cars = src.main:main"]}
)