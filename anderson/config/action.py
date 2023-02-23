from abc import ABC, abstractmethod
from typing import Union

from pydantic import BaseModel, PositiveInt


class Action(BaseModel, ABC):
    """An abstract dataclass class for a script action."""

    @abstractmethod
    def to_bash_command(self) -> str:
        """
        Convert the action into an asciinema_automation bash command.

        :return: An asciinema_automation bash command.
        """
        raise NotImplementedError


class EnterAction(Action):
    """An action that enters some symbols."""

    enter: str

    def to_bash_command(self) -> str:
        return self.enter


class ExpectAction(Action):
    """An action that waits for some symbols."""

    expect: str

    def to_bash_command(self) -> str:
        return f'#$ expect {self.expect}'


class WaitAction(Action):
    """An action that waits a number of seconds."""

    wait: PositiveInt

    def to_bash_command(self) -> str:
        return f'#$ wait {self.wait}'


class DelayAction(Action):
    """An action that sets delay between keystrokes."""

    delay: PositiveInt

    def to_bash_command(self) -> str:
        return f'#$ delay {self.delay}'


ActionType = Union[EnterAction, WaitAction, ExpectAction, DelayAction]
