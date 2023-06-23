import os
import re
import stat
from pathlib import Path
from platform import libc_ver, machine, system
from typing import List, Optional
from urllib.request import urlretrieve

from setuptools import find_packages, setup

from anderson.utils import AGG_PATH

VERSION = '0.3.0'
AGG_VERSION = '1.4.2'

REQUIREMENTS_FILE = Path(__file__).parent / 'requirements.txt'


def get_requires() -> List[str]:
    with open(REQUIREMENTS_FILE) as requirements_file:
        return [re.sub(r'(git\+.*egg=(.*))', r'\2 @ \1', line) for line in requirements_file.read().split('\n')]


def get_agg_bin_name() -> Optional[str]:  # noqa: WPS231
    agg_bin_name = None

    if system() == 'Darwin':
        if machine() in {'arm64', 'aarch64_be', 'aarch64', 'armv8b', 'armv8l'}:
            agg_bin_name = 'agg-aarch64-apple-darwin'
        elif machine() in {'x86_64', 'x64'}:
            agg_bin_name = 'agg-x86_64-apple-darwin'

    elif system() == 'Linux':
        if machine() in {'arm64', 'aarch64_be', 'aarch64', 'armv8b', 'armv8l'}:
            agg_bin_name = 'agg-aarch64-unknown-linux-gnu'

        elif machine() == 'arm':
            agg_bin_name = 'agg-arm-unknown-linux-gnueabihf'

        elif machine() in {'x86_64', 'x64'}:
            if libc_ver()[0] in {'glibc', 'libc'}:
                agg_bin_name = 'agg-x86_64-unknown-linux-gnu'
            else:
                agg_bin_name = 'agg-x86_64-unknown-linux-musl'

    return agg_bin_name


def download_agg_bin() -> None:
    agg_bin_name = get_agg_bin_name()
    if agg_bin_name is None:
        raise ValueError('There is no agg executable for this system.')

    AGG_PATH.parent.mkdir(parents=True, exist_ok=True)
    urlretrieve(  # noqa: S310
        url=f'https://github.com/asciinema/agg/releases/download/v{AGG_VERSION}/{agg_bin_name}',
        filename=AGG_PATH,
    )

    os.chmod(AGG_PATH, os.stat(AGG_PATH).st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


download_agg_bin()


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
        'Operating System :: MacOS',
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
