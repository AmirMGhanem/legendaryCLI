from setuptools import setup, find_packages

setup(
    name="legendarycli",
    author="Amir M. Ghanem",
    author_email="amirghanem95@gmail.com",
    version='0.0.8',
    description="This is a simple CLI to show my CV and resume",
    long_description=open('long_desc.txt').read(),
    url="https://github.com/AmirMGhanem/legendaryCLI",
    github="https://www.github.com/AmirMGhanem",
    packages=find_packages(),
    install_requires=[
        'Click',
        'termcolor',
        'pyfiglet',
        'requests',
        'tqdm'
    ],
    entry_points='''
        [console_scripts]
        legendarycli=legendarycli.__init__:init
    ''',
    classifiers=[
        "Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)


