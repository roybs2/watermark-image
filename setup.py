import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="watermarkImage",
    version="1.0.2",
    description="Watermark batch of images",
    long_description=README,
    long_description_content_type="text/markdown",
    download_url="https://github.com/roybs2/watermark-image/archive/v1.0.1.tar.gz",
    url="https://github.com/roybs2/watermark-image",
    author="Roy Ben Shlomo",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
    ],
    packages=["watermarkImage"],
    include_package_data=True,
    install_requires=["pillow"],
    entry_points={"console_scripts": ["watermarkImage=watermarkImage.Logic:main"]},
)