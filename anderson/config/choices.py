from enum import Enum
from typing import List


class Theme(Enum):
    # Consistent with https://github.com/asciinema/agg/blob/4b605b6eb670bfaba2cfda1cb258cfbfdfc1f2d4/src/main.rs#L43
    ASCIINEMA = 'asciinema'
    DRACULA = 'dracula'
    MONOKAY = 'monokai'
    SOLARIZED_DARK = 'solarized_dark'
    SOLARIZED_LIGHT = 'solarized_light'

    @classmethod
    def values(cls) -> List[str]:
        return [theme.value for theme in cls]

    def to_hex(self) -> List[str]:
        theme_to_hex = {
            self.ASCIINEMA: [
                '121314',
                'cccccc',
                '000000',
                'dd3c69',
                '4ebf22',
                'ddaf3c',
                '26b0d7',
                'b954e1',
                '54e1b9',
                'd9d9d9',
                '4d4d4d',
                'dd3c69',
                '4ebf22',
                'ddaf3c',
                '26b0d7',
                'b954e1',
                '54e1b9',
                'ffffff',
            ],
            self.DRACULA: [
                '282a36',
                'f8f8f2',
                '21222c',
                'ff5555',
                '50fa7b',
                'f1fa8c',
                'bd93f9',
                'ff79c6',
                '8be9fd',
                'f8f8f2',
                '6272a4',
                'ff6e6e',
                '69ff94',
                'ffffa5',
                'd6acff',
                'ff92df',
                'a4ffff',
                'ffffff',
            ],
            self.MONOKAY: [
                '272822',
                'f8f8f2',
                '272822',
                'f92672',
                'a6e22e',
                'f4bf75',
                '66d9ef',
                'ae81ff',
                'a1efe4',
                'f8f8f2',
                '75715e',
                'f92672',
                'a6e22e',
                'f4bf75',
                '66d9ef',
                'ae81ff',
                'a1efe4',
                'f9f8f5',
            ],
            self.SOLARIZED_DARK: [
                '002b36',
                '839496',
                '073642',
                'dc322f',
                '859900',
                'b58900',
                '268bd2',
                'd33682',
                '2aa198',
                'eee8d5',
                '002b36',
                'cb4b16',
                '586e75',
                '657b83',
                '839496',
                '6c71c4',
                '93a1a1',
                'fdf6e3',
            ],
            self.SOLARIZED_LIGHT: [
                'fdf6e3',
                '657b83',
                '073642',
                'dc322f',
                '859900',
                'b58900',
                '268bd2',
                'd33682',
                '2aa198',
                'eee8d5',
                '002b36',
                'cb4b16',
                '586e75',
                '657c83',
                '839496',
                '6c71c4',
                '93a1a1',
                'fdf6e3',
            ],
        }

        return theme_to_hex[self]


class FontFamily(str, Enum):  # noqa: WPS600
    # Consistent with https://github.com/asciinema/agg/blob/4b605b6eb670bfaba2cfda1cb258cfbfdfc1f2d4/src/main.rs#L136
    JETBRAINS_MONO = 'JetBrains Mono'
    FIRA_CODE = 'Fira Code'
    SF_MONO = 'SF Mono'
    MENLO = 'Menlo'
    CONSOLAS = 'Consolas'
    DEJAVU_SANS_MONO = 'DejaVu Sans Mono'
    LIBERATION_MONO = 'Liberation Mono'
