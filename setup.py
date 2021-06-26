from setuptools import setup
from pyrrole import __author__, __email__, __version__, __homepage__

with open("README.md") as fh:
    long_description = fh.read()

setup(
    name='pyrrole',
    version=__version__,
    packages=['pyrrole'],
    url=__homepage__,
    license='GNU General Public License v3.0',
    author=__author__,
    author_email=__email__,
    maintainer=__author__,
    maintainer_email=__email__,
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Operating System :: OS Independent",
        ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    description='Role system for Python3',
    keywords='pyrrole role roles moose perl',
    python_requires='>=3.6'

)
