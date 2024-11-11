from gameloop import GameLoop


class PvpGameLoop(GameLoop):
    def __init__(self):
        self.message = ''

    def run(self):
        self.message = 'zsaaa'
        print(self.message)
