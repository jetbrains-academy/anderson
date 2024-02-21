import os
import stat
from platform import libc_ver, machine, system
from typing import Optional
from urllib.request import urlretrieve

from anderson.utils import AGG_PATH

AGG_VERSION = '1.4.2'


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
