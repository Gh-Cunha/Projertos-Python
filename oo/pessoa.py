class Pessoa:
    def __init__(self, *filhos, nome=None, idade=23):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    Gabriel = Pessoa(nome = 'Gabriel')
    Henrique = Pessoa(Gabriel, nome='Henrique')
    print(Pessoa.cumprimentar(Henrique))
    print(id(Henrique))
    print(Henrique.cumprimentar())
    print(Henrique.nome)
    print(Henrique.idade)
    for filho in Henrique.filhos:
        print(filho.nome)
    Henrique.sobrenome = "Cunha"
    del Henrique.filhos
    print(Henrique.__dict__)
    print(Gabriel.__dict__)