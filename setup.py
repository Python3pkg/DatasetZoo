from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Dataset_Zoo',
    packages=["Dataset_Zoo"],
    version='1.0.0',
    description='Easily share datasets within your institution\
    or with the rest of the world!',
    long_description=long_description,
    # The project's main homepage.
    url='https://github.com/IanQS/Dataset-Zoo',
    download_url='https://github.com/peterldowns/mypackage/tarball/0.1',

    # Author details
    author='Ian Quah',
    author_email='itq@andrew.cmu.edu',

    license='MIT',

    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
    ],

    # What does your project relate to?
    keywords=['research datasets download upload'],

    # These will be installed by pip when
    # your project is installed.
    install_requires=['requests', 'h5py', 'urllib2'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
)
