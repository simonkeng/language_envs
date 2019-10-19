from setuptools import setup

setup(
    name='rsr',
    version='0.0.2',
    py_modules=['rsr'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        rsr=rsearch_script:cli
    ''',
)
