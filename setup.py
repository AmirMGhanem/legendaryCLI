from setuptools import setup,find_packages

setup(
    name="legendarycli",
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'Click',
        'termcolor',
        'pyfiglet'
    ],
    entry_points='''
        [console_scripts]
        legendarycli=cli:init
    ''',
)