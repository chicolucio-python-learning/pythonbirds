class Pessoa:
    def __init__(self, nome=None, idade=31):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == "__main__":
    p = Pessoa('Francisco')
    print(Pessoa.cumprimentar(p))  # desnecessário
    print(id(p))
    print(p.cumprimentar())  # p passado implicitamente
    print(p.nome)
    p.nome = 'Francisco'
    print(p.idade)
