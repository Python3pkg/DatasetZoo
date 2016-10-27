from setuptools import setup  # , find_packages

# To use a consistent encoding

version = '1.2.6'

packages = [
    "DatasetZoo",
    "DatasetZoo.utils",
    "DatasetZoo.downloaded_datasets"]

setup(
    name='DatasetZoo',
    packages=packages,
    version=version,
    description='Easily share datasets within your institution\
    or with the rest of the world!',
    # The project's main homepage.
    url='https://github.com/IanQS/DatasetZoo',
    download_url='https://github.com/IanQS/DatasetZoo/releases/tag/' + version,
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
        'Programming Language :: Python :: 3.5'
    ],

    # What does your project relate to?
    keywords=['research datasets download'],

    # These will be installed by pip when
    # your project is installed.
    install_requires=['requests', 'h5py', 'clint'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    extras_require={
        'dev': ['check-manifest', 'urllib2'],
        'test': ['coverage'],
    },
)
