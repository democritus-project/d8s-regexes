#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from regexes import __version__

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read().splitlines()

with open('requirements_dev.txt') as requirements_dev_file:
    test_requirements = requirements_dev_file.read().splitlines()

setup(
    name='democritus_regexes',
    version=__version__,
    description="Democritus functions for working with regexes in Python.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Floyd Hightower",
    author_email='floyd.hightower27@gmail.com',
    url='https://github.com/democritus/democritus-regexes',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    packages=find_packages(exclude=('tests')),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=True,
    keywords='regexes',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
