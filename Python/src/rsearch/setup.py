from setuptools import setup

setup(
    name='rsearch',
    version='0.0.1',
    py_modules=['rsearch'],
    entry_points={
        'console_scripts': [
            'rsearch=rsearch.__main__:main'
        ]
    }
)
