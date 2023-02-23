import re
from pathlib import Path
from typing import List

from setuptools import setup, find_packages

VERSION = "1.0.0"


REQUIREMENTS_FILE = Path(__file__).parent / 'requirements.txt'


def get_requires() -> List[str]:
    with open(REQUIREMENTS_FILE) as requirements_file:
        return [re.sub(r'(git\+.*egg=(.*))', r'\2 @ \1', line) for line in requirements_file.read().split('\n')]


setup(
    name='anderson',
    version=VERSION,
    author='Ilya Vlasov',
    author_email='ilyavlasov2011@gmail.com',
    description='A tool for automatically recording a terminal session into animated GIF files',
    long_description='file: README.md',
    long_description_content_type='text/markdown',
    url='https://github.com/GirZ0n/anderson',
    license='Apache License 2.0',
    license_files='LICENSE',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Education',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Topic:: Utilities',
    ],
    python_requires='>=3.8, <4',
    install_requires=get_requires(),
    include_package_data=True,
    package_data={'anderson': ['bin/*']},
    packages=find_packages(),
    entry_points={'console_scripts': ['anderson=anderson.main:main']},
)
