import logging
import shlex
import subprocess
from pathlib import Path
from platform import system
from typing import List

AGG_PATH = Path(__file__).parent / 'bin' / 'agg.exe' if system() == 'Windows' else 'agg'

logger = logging.getLogger(__name__)


def run_in_subprocess(command: List[str]) -> int:
    logger.debug(f'Running {shlex.join(command)}')

    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout = process.stdout.decode() if process.stdout else None
    stderr = process.stderr.decode() if process.stderr else None

    if stdout:
        logger.debug(f"{command[0]}'s stdout:\n{stdout}")

    if stderr:
        logger.debug(f"{command[0]}'s stderr:\n{stderr}")

    return process.returncode
