
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Topsis",
    version="1.0.4",
    author="Anshika Singla",
    author_email="asingla2_be20@thapar.edu,
    description="A package -> Calculates Topsis Score and Rank them accordingly",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/Anshi-1234/102003458_topsis",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["102003458_topsis"],
    include_package_data=True,
    install_requires='pandas',
    entry_points={
        "console_scripts": [
            "topsis=102003458_topsis.topsis:main",
        ]
    },
)
