from setuptools import setup

setup(
    name='sqlstrings',
    version='0.0.5',
    description='A Python library for generating strings in different SQL dialects.',
    package_dir={'sqlstrings':'src'},
    py_modules=['csv_handling', 'postgre', 'transact', 'value_handling'],
    url='https://github.com/alikellaway/sqlstrings',
    author='Ali Kellaway',
    author_email='ali.kellaway139@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='sql database python library strings generate',
    python_requires='>=3.8, <4',
)