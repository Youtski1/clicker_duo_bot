from dataclasses import dataclass
from .answers import answers
from .greetings import greetings
from .stages import stages
from .avatars import avatars


@dataclass
class DialogData:
    avatars = avatars
    greetings = greetings
    answers = answers
    stages = stages



