from setuptools import setup

setup(
    name='r-search',
    version='0.0.1',
    packages=['r-search'],
    entry_points={
        'console_scripts': [
            'r-search=__main__:main'
        ]
    }
)
