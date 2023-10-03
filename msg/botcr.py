from botcr import BotCr


class MsgBot(BotCr):
    def run(self):
        print('Executa MsgBot')

    def info(self):
        print(f'Esse é o MsgBot: {self.nome}')


if __name__ == '__main__':
    bot = MsgBot('MSG-BOT')
    bot.info()
    bot.run()
