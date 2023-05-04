from setuptools import setup
from setuptools import find_packages


if __name__ == "__main__":
    setup(
        packages=find_packages(),
        package_data={"": ["*.json", ".yaml"]},
        include_package_data=True,
    )
