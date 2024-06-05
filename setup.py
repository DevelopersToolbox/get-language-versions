# setup.py

"""Setup script."""

from setuptools import setup

with open('requirements.txt', 'r', encoding='UTF-8') as f:
    required: list[str] = f.read().splitlines()

with open("README.md", 'r', encoding='UTF-8') as f:
    long_description: str = f.read()

setup(
    name='wolfsoftware.get-language-versions',
    version='0.1.0',
    packages=['wolfsoftware.get_language_versions'],
    entry_points={
        'console_scripts': [
            'get-language-versions=wolfsoftware.get_language_versions.main:main',
        ],
    },
    author='Wolf Software',
    author_email='pypi@wolfsoftware.com',
    description='A nice description will go here',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/DevelopersToolbox/get-language-verisons',
    project_urls={
        ' Source': 'https://github.com/DevelopersToolbox/get-language-verisons',
        ' Tracker': 'https://github.com/DevelopersToolbox/get-language-verisons/issues/',
        ' Documentation': 'https://github.com/DevelopersToolbox/get-language-verisons',
        ' Funding': 'https://ko-fi.com/wolfsoftware',
        ' Say Thanks!': 'https://github.com/sponsors/TGWolf',
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
    ],
    python_requires='>=3.9',
    install_requires=required,
)
