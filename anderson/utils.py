import logging
import shlex
import subprocess
from pathlib import Path
from typing import List

PROJECT_ROOT = Path(__file__).parents[1]
AGG_PATH = PROJECT_ROOT / 'anderson' / 'bin' / 'agg'

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
