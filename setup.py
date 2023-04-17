from setuptools import setup, find_packages

setup(
    name='sqlstrings',
    version='0.0.3',
    description='A Python library for generating strings in different SQL dialects.',
    url='https://github.com/alikellaway/sqlstrings',
    author='Ali Kellaway',
    author_email='ali.kellaway139@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # TODO Research licenses.
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='sql database python library strings generate',
    package_dir={'':'src'},
    install_requires=[],
    python_requires='>=3.8, <4',
)