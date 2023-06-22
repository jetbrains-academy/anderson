import os
from pathlib import Path
from anderson.utils import run_in_subprocess
from test import EXAMPLES_FOLDER
from test.utils import LocalCommandBuilder
from tempfile import TemporaryDirectory, gettempdir
import pytest
from PIL import Image
from PIL.ImageSequence import Iterator
from PIL.ImageChops import difference

GIF_GENERATION_TEST_DATA = [
    (
        f'python3 {EXAMPLES_FOLDER / "python_bot" / "main.py"}',
        EXAMPLES_FOLDER / 'python_bot' / 'config.yaml',
        EXAMPLES_FOLDER / 'python_bot' / 'gifs',
    ),
    # TODO: uncomment this test case when AGG will generate the same gifs on different platforms
    # (
    #     f'kotlinc {EXAMPLES_FOLDER / "kotlin_calculator" / "Main.kt"} '
    #     f'-include-runtime -d {gettempdir()}/Main.jar && java -jar {gettempdir()}/Main.jar',
    #     EXAMPLES_FOLDER / 'kotlin_calculator' / 'config.yaml',
    #     EXAMPLES_FOLDER / 'kotlin_calculator' / 'gifs',
    # ),
]


@pytest.mark.parametrize(('executable', 'config', 'expected_output'), GIF_GENERATION_TEST_DATA)
def test_gif_generation(executable: str, config: Path, expected_output: Path):
    with TemporaryDirectory() as actual_output:
        command_builder = LocalCommandBuilder(executable, actual_output, config)
        run_in_subprocess(command_builder.build())

        expected_gifs = {
            file: expected_output / file
            for file in os.listdir(expected_output)
            if os.path.isfile(expected_output / file)
        }

        actual_gifs = {
            file: Path(actual_output) / file
            for file in os.listdir(actual_output)
            if os.path.isfile(Path(actual_output) / file)
        }

        assert len(expected_gifs) == len(actual_gifs) != 0

        for actual_gif_name, actual_gif_path in actual_gifs.items():
            assert actual_gif_name in expected_gifs.keys()

            with Image.open(actual_gif_path) as actual_gif, Image.open(expected_gifs[actual_gif_name]) as expected_gif:
                for actual_frame, expected_frame in zip(Iterator(actual_gif), Iterator(expected_gif)):
                    assert difference(actual_frame.convert('RGB'), expected_frame.convert('RGB')).getbbox() is None
