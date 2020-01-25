class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=31):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_classe = super().cumprimentar()
        return f'{cumprimentar_classe}. Aperto de mão'


class Mutante(Pessoa):
    olhos = 3


if __name__ == "__main__":
    francisco = Mutante(nome='Francisco')
    jose = Homem(francisco, nome='Jose')
    print(jose.filhos)
    for filho in jose.filhos:
        print(filho.nome)

    jose.sobrenome = 'Bustamante'
    print(jose.sobrenome)

    print(francisco.__dict__)
    print(jose.__dict__)

    del jose.filhos

    print(jose.__dict__)

    print(Pessoa.olhos)
    print(id(Pessoa.olhos))
    print(jose.olhos)
    print(id(jose.olhos))
    print(francisco.olhos)
    print(id(francisco.olhos))
    print(Pessoa.metodo_estatico(), francisco.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(),
          francisco.nome_e_atributos_de_classe())

    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(francisco, Pessoa))
    print(isinstance(francisco, Homem))
    print(francisco.olhos)
    print(jose.cumprimentar())
    print(francisco.cumprimentar())
