from dataclasses import dataclass
from pathlib import Path
from typing import List, Union


@dataclass
class LocalCommandBuilder:
    executable: str
    output: Union[Path, str]
    config: Union[Path, str]
    debug: bool = True

    def build(self) -> List[str]:
        command = [
            'anderson',
            self.executable,
            str(self.output),
            str(self.config),
        ]

        if self.debug:
            command.append('--debug')

        return command
