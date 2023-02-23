import argparse
import logging
import sys
from contextlib import contextmanager
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import List

from asciinema_automation.script import Script

from pydantic import ValidationError

import yaml

from anderson.config.action import Action
from anderson.config.model import Config, Gif
from anderson.utils import AGG_PATH, run_in_subprocess

logger = logging.getLogger(__name__)


def configure_parser(parser: argparse.ArgumentParser) -> None:
    parser.add_argument('executable', type=str, help='Executable to record.')
    parser.add_argument('output', type=lambda value: Path(value).absolute(), help='Path where to save gifs.')
    parser.add_argument('config', type=lambda value: Path(value).absolute(), help='Path to a config file.')
    parser.add_argument('--debug', action='store_true', help='Enable debug logging.')


@contextmanager
def create_script_file(script: List[Action]) -> Path:
    """
    Write the list of actions to a temporary bash file in an asciinema_automation format and yield its path.

    This function must be used as a context manager. On exit, the temporary file will be deleted.

    :param script: List of actions.
    :return: Path to an asciinema_automation script file.
    """
    logger.info('Creating the script file.')
    with NamedTemporaryFile(mode='w', suffix='.sh') as script_file:
        for command in script:
            script_file.write(f'{command.to_bash_command()}\n')

        yield Path(script_file.name)


def create_gif_generation_command(cast_file: Path, output_dir: Path, gif: Gif) -> List[str]:
    """
    Create a gif generation command for agg (asciinema gif generator).

    :param cast_file: Path to a cast file that will be converted to a gif.
    :param output_dir: Path where the generated gif will be saved.
    :param gif: Gif preferences.
    :return: Gif generation command as a list of strings.
    """
    command = [
        str(AGG_PATH),
        str(cast_file),
        str(output_dir / f'{gif.name}.gif'),
        '--theme',
        ','.join(gif.theme),
        '--font-family',
        gif.font_family,
        '--font-size',
        str(gif.font_size),
        '--fps-cap',
        str(gif.fps_cap),
        '--line-height',
        str(gif.line_height),
        '--speed',
        str(gif.speed),
    ]

    if gif.no_loop:
        command.append('--no-loop')

    return command


def main() -> int:
    parser = argparse.ArgumentParser()
    configure_parser(parser)

    args = parser.parse_args()

    logging.basicConfig(
        format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
        level=logging.DEBUG if args.debug else logging.INFO,
    )

    logger.info('Reading the config file.')

    with open(args.config) as f:
        config_data = yaml.safe_load(f)

    try:
        config = Config.parse_obj(config_data)
    except ValidationError as e:
        logger.error(e)
        return 1

    script = config.script
    terminal_config = config.terminal_config
    interaction_config = config.interaction_config
    gif_config = config.gif_config

    with NamedTemporaryFile(suffix='.cast') as cast_file:
        with create_script_file(script) as script_path:
            logger.info('Recording the executable.')
            Script(
                script_path,
                Path(cast_file.name),
                f'-c "{args.executable}" --cols {terminal_config.cols} --rows {terminal_config.rows}',
                wait=interaction_config.instruction_delay,
                delay=interaction_config.keystroke_delay,
                standart_deviation=interaction_config.keystroke_std,
            ).execute()

        args.output.mkdir(parents=True, exist_ok=True)
        for gif in gif_config.gifs:
            logger.info(f'Generating {gif.name}.gif')
            run_in_subprocess(create_gif_generation_command(Path(cast_file.name), args.output, gif))


if __name__ == '__main__':
    sys.exit(main())
