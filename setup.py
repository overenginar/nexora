from setuptools import setup
from setuptools import find_packages


if __name__ == "__main__":
    setup(
        package_dir={"": "src"},
        packages=find_packages("src"),
        package_data={"": ["*.json", "*.yaml", "*.ini"]},
        include_package_data=True,
    )
