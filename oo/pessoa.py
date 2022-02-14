class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=23):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos{cls.olhos}'
class Homem (Pessoa):
    pass

if __name__ == '__main__':
    Gabriel = Homem(nome = 'Gabriel')
    Henrique = Homem(Gabriel, nome='Henrique')
    print(Pessoa.cumprimentar(Henrique))
    print(id(Henrique))
    print(Henrique.cumprimentar())
    print(Henrique.nome)
    print(Henrique.idade)
    for filho in Henrique.filhos:
        print(filho.nome)
    Henrique.sobrenome = "Cunha"
    del Henrique.filhos
    Henrique.olhos = 1
    del Henrique.olhos
    print(Henrique.__dict__)
    print(Gabriel.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(Henrique.olhos)
    print(Gabriel.olhos)
    print(id(Pessoa.olhos), id(Henrique.olhos), id(Gabriel.olhos))
    print(Pessoa.metodo_estatico(), Henrique.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), Henrique.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(Henrique, Pessoa))
    print(isinstance(Henrique, Homem))
