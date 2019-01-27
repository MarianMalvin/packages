import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-marian",
    version="0.0.1",
    author="Marian Zozulia",
    author_email="mzozulia@cloudferro.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.cloudferro.com/mzozulia/utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
