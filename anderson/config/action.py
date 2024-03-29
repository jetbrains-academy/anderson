from abc import ABC, abstractmethod
from typing import Union

from pydantic import BaseModel, PositiveInt


class Action(BaseModel, ABC):
    """Abstract dataclass class for a scenario action."""

    @abstractmethod
    def to_bash_command(self) -> str:
        """
        Convert the action into an asciinema_automation bash command.

        :return: asciinema_automation bash command.
        """
        raise NotImplementedError


class WriteAction(Action):
    """Action that writes some symbols and presses enter."""

    write: str

    def to_bash_command(self) -> str:
        return self.write


class SendAction(Action):
    """Action that writes some symbols (without pressing enter)."""

    send: str

    def to_bash_command(self) -> str:
        return f'#$ send {self.send}'


class ExpectAction(Action):
    """Action that expects some symbols to be printed."""

    expect: str

    def to_bash_command(self) -> str:
        return f'#$ expect {self.expect}'


class WaitAction(Action):
    """Action that waits a number of seconds."""

    wait: PositiveInt

    def to_bash_command(self) -> str:
        return f'#$ wait {self.wait}'


class DelayAction(Action):
    """Action that sets delay between keystrokes."""

    delay: PositiveInt

    def to_bash_command(self) -> str:
        return f'#$ delay {self.delay}'


class ControlAction(Action):
    """Action that sends control character."""

    ctrl: str

    def to_bash_command(self) -> str:
        return f'#$ sendcontrol {self.ctrl}'


class PressAction(Action):
    """Action that press some key."""

    press: str

    def to_bash_command(self) -> str:
        return f'#$ sendcharacter {self.press}'


ActionType = Union[WriteAction, WaitAction, ExpectAction, DelayAction, ControlAction, SendAction, PressAction]
