class BotCr:
    def __init__(self, nome):
        self.nome = nome
        print(f'Construtor da Classe Mãe BotCr!')

    def run(self):
        print('Executa da Classe Mãe BotCr!')

    def info(self):
        print(f'Este é o BotCr: {self.nome}')


if __name__ == '__main__':
    bot = BotCr('BOT-CR')
    bot.info()
    bot.run()
