import random as rnd
class rnd_msg:
    messages = [
        "You are beautiful!",
        "Words can’t explain what a wonderful person you are.",
        "You look what a sweet pie here!"
    ]

    def get_msg(self):
        msg = rnd.choice(self.messages)
        return msg        
    pass