class Pessoa:
    def __init__(self, *filhos, nome=None, idade=31):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == "__main__":
    francisco = Pessoa(nome='Francisco')
    jose = Pessoa(francisco, nome='Jose')
    print(jose.filhos)
    for filho in jose.filhos:
        print(filho.nome)
