from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.2'
DESCRIPTION = 'A library for creating text-based games in the terminal'

# Setting up
setup(
    name="text-based-lib",
    version=VERSION,
    author="gugu256 (Gustave Dufresne-Walter)",
    author_email="gugu256@mail.com",
    url="https://tblib-docs.devplodocus.repl.co",
    license="MIT License",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['colorama'],
    keywords=['python', 'lightweight', 'game-development', 'terminal-based', 'terminal-game', 'text-based-game'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)