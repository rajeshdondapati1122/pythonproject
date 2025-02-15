from setuptools import setup, find_packages

setup(
    name="pythonproject",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pytest",
    ],
    entry_points={
        "console_scripts": [
            "pythonproject=main:main",
        ],
    },
)
