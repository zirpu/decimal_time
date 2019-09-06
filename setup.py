"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="decimal_time",
    version="0.1.0",
    description="Decimal Time utilities and a cli.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/zirpu/decimal_time",
    author="allan bailey",
    author_email="allan@zirpu.org",
    classifiers=[  # Optional
        # For a list of valid classifiers, see https://pypi.org/classifiers/
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Environment :: Console",
        # Pick your license as you wish
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    # keywords='',  # Optional
    packages=find_packages(),  # (exclude=["decimal_time"]),
    python_requires=">=3.6, <4",
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    # install_requires=[],  # Optional
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    # extras_require={"dev": ["check-manifest"], "test": ["coverage"]},
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    entry_points={"console_scripts": ["decimal_time=decimal_time.decimal_time:main"]},
)
