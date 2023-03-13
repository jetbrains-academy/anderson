import re
from typing import Any, List

from pydantic import BaseModel, NonNegativeInt, PositiveFloat, PositiveInt, conlist, validator

from anderson.config.action import ActionType
from anderson.config.choices import Theme


class TerminalConfig(BaseModel):
    cols: PositiveInt = 80
    rows: PositiveInt = 24


class InteractionConfig(BaseModel):
    keystroke_delay: NonNegativeInt = 150
    keystroke_std: NonNegativeInt = 60
    action_delay: NonNegativeInt = 80


class Gif(BaseModel):
    name: str
    theme: List[str] = Theme.DRACULA.to_hex()
    font_family: str = 'JetBrains Mono,Liberation Mono,Andale Mono'
    font_size: PositiveInt = 14
    fps_cap: PositiveInt = 30
    line_height: PositiveFloat = 1.4
    speed: PositiveFloat = 1.0
    no_loop: bool = False

    @validator('font_family', pre=True)
    def check_font_family_list(cls, value: Any) -> Any:  # noqa: N805
        if isinstance(value, list) and not all(isinstance(elem, str) for elem in value):
            raise ValueError('the list must contain only strings')

        return value

    @validator('font_family', pre=True)
    def convert_font_family(cls, value: Any) -> Any:  # noqa: N805
        if isinstance(value, list):
            return ','.join(value)

        return value

    @validator('theme', pre=True)
    def convert_string_theme_to_list(cls, value: Any) -> Any:  # noqa: N805
        if isinstance(value, str):
            if value in Theme.values():
                return Theme(value).to_hex()

            raise ValueError(f'value is not a valid enumeration member; permitted: {", ".join(Theme.values())}')

        return value

    @validator('theme', pre=True)
    def check_theme_list_size(cls, value: Any) -> Any:  # noqa: N805
        if isinstance(value, list) and len(value) != 10 and len(value) != 18:  # noqa: WPS432
            raise ValueError('the list must contain exactly 10 or 18 items')
        return value

    @validator('theme', each_item=True)
    def check_hex_color(cls, value: Any) -> Any:  # noqa: N805
        regex = '[0-9a-fA-F]{6}'
        if isinstance(value, str) and not re.match(regex, value):
            raise ValueError(f'the list items must be in hex color format (regex: {regex})')
        return value


class GifConfig(BaseModel):
    gifs: conlist(Gif, min_items=1)

    def __init__(self, **data):
        common_data = data.pop('common', {})

        new_data = {'gifs': []}
        for gif in data['gifs']:
            new_gif = common_data.copy()
            new_gif.update(gif)
            new_data['gifs'].append(new_gif)

        super().__init__(**new_data)


class Config(BaseModel):
    terminal_config: TerminalConfig = TerminalConfig()
    interaction_config: InteractionConfig = InteractionConfig()
    gif_config: GifConfig
    scenario: conlist(ActionType, min_items=1)
