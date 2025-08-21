import random
from ..dialog_data import DialogData
from ..config import best_id, best_symbol

from ..types import (
    Duo,
    User
)

import logging
logger = logging.getLogger(__name__)

class DialogService:
    
    def __init__(
        self,
        duo: Duo,
        user: User,
        dialog_data: DialogData = DialogData()
    ):
        self.duo = duo
        self.user = user
        self.dialog_data = dialog_data

    def greeting(self):
        greeting = random.choice(self.dialog_data.greetings[self.duo.stage])
        name = self.name()
        return greeting.format(name=name)

    def name(self):
        stage = self.duo.stage
        name = self.user.full_name

        if stage > 3:
            percent = 3 if stage == 4 else 2 
            name_list = list(name)
            indexs = [i for i in range(len(name_list)-1)]
            symbols = ["^","$","@","*","!","~"]

            for i in range(len(name)//percent):
                index = random.choice(indexs)
                symbol = random.choice(symbols)
                name_list[index] = symbol
            name = ''.join(name_list)

        if self.user.telegram_id == best_id:
            name = f"{best_symbol} {name} {best_symbol}"
        
        return name
    
    def avatar(self):
        return self.dialog_data.avatars[self.duo.stage]

    def answer(
        self,
        key: str
    ):
        answers = self.dialog_data.answers[key][self.duo.stage]
        
        if type(answers) == list:
            return random.choice(answers)
        else: 
            return answers
      
    def stage(self):
        stages = self.dialog_data.stages[self.duo.stage]
        return random.choice(stages)
    
    def start(self):
        greeting = self.greeting()
        stage = self.stage()

        if self.duo.health == 0:
            answer = self.dialog_data.answers["start_recovery"]
        else:
            answer = self.answer(key="start")

        return f"{greeting}\n\n{answer}\n\n💬 Duo: {stage}"

    def profile(self):
        answer = self.answer(key="profile")
        name = self.name()
        stage = self.stage()

        answerf = answer.format(
            name=name,
            feathers=self.user.feathers,
            damage=self.user.damage,
            level=self.duo.level
        )

        return f"{answerf}\n\n💬 Duo: {stage}"
    
    def upgrade_damage(
        self,
        status: bool
    ):
        answer = self.dialog_data.answers["upgrade_damage"]

        if status:
            text = answer[status][self.duo.stage]
            return text
        else:
            feathers_difference = (300 * self.user.damage + 900) - self.user.feathers
            text = answer[status].format(feathers=feathers_difference)
            return text




