class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=31):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


if __name__ == "__main__":
    francisco = Pessoa(nome='Francisco')
    jose = Pessoa(francisco, nome='Jose')
    print(jose.filhos)
    for filho in jose.filhos:
        print(filho.nome)

    jose.sobrenome = 'Bustamante'
    print(jose.sobrenome)

    francisco.olhos = 1

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
