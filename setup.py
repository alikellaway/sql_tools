from setuptools import setup
from pathlib import Path

setup(
    name='sqlstrings',
    version='0.0.9',    
    description='Generates SQL query strings in multiple dialects.',
    long_description= (Path(__file__).parent / "README.md").read_text(),
    keywords='sql strings generate query',
    url='https://github.com/alikellaway/sqlstrings',
    author='Ali Kellaway',
    author_email='ali.kellaway139@gmail.com',
    license='MIT',
    # package_dir={'':''},
    packages=['sqlstrings'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',         
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent'
    ]
)