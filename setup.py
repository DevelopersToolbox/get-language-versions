# setup.py

"""Setup script."""

from setuptools import setup, find_packages

with open('requirements.txt', 'r', encoding='UTF-8') as f:
    required: list[str] = f.read().splitlines()

with open("README.md", 'r', encoding='UTF-8') as f:
    long_description: str = f.read()

setup(
    name='get-language-versions',
    version='0.0.1rc1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'get-language-versions=get_language_versions.main:main',
        ],
    },
    author='Wolf Software',
    author_email='pypi@wolfsoftware.com',
    description='A nice description will go here',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/DevelopersToolbox/get-language-verisons',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
    install_requires=required,
)
