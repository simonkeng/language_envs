from setuptools import setup

setup(
    name='rsearch',
    version='0.0.1',
    py_modules=['rsearch'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        rsearch=rsearch_script:cli
    ''',
)
