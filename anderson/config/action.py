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
    """Action that writes some symbols."""

    write: str

    def to_bash_command(self) -> str:
        return self.write


class ExpectAction(Action):
    """Action that waits for some symbols."""

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


ActionType = Union[EnterAction, WaitAction, ExpectAction, DelayAction]
