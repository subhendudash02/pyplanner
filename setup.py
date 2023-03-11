import setuptools

with open("README.md", "r") as f:
    description = f.read()

setuptools.setup(
    name="pyagenda",
    version="0.0.1",
    author="Subhendu Dash",
    author_email="sdash29102@gmail.com",
    description="pyagenda keeps track of all your activities and notifies you when they are due",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/subhendudash02/pyagenda",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.8',
)