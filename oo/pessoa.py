class Pessoa:
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == "__main__":
    p = Pessoa()
    print(Pessoa.cumprimentar(p))  # desnecessário
    print(id(p))
    print(p.cumprimentar())  # p passado implicitamente
