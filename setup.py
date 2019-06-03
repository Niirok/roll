import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rolled",
    version="0.0.1",
    author="Anthony YOUSSEF",
    author_email="Anthony_Youssef@hotmail.fr",
    description="A small package for people forgetting their dices at home....",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Niirok/roll",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
