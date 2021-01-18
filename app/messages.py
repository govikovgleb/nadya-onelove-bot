import random as rnd
class MessagesGenerator:
    messages = [
        "You are beautiful!",        
        "Look what a sweet pie here!",
        "Bark!",
        "WOOF!",
        "Meow :3",
        "Thanks, sweetheart",
        "Oh, your finger is so soft!",
        "It makes me feel so good!"        
    ]
    
    def __init__(self):
        self.last_message = None

    def __repr__(self):
        res = f'{self.__class__.__name__}({id(self)})'
        return res

    def get_msg(self):
        msg = rnd.choice(self.messages)
        
        if self.last_message == msg:
            if len(self.messages) > 1:
                return self.get_msg()

        self.last_message = msg
        return msg