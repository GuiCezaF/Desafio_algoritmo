'''
Alunos: Guilherme Cezarino, Felipe Zamariolli, Gabriel Eduardo
'''




import unittest
from desafio_func import herdeiros


Familia = [
    
    {'nome': 'Eduardo', 'pai': None},
    {'nome': 'Lucas', 'pai': 'Eduardo'},
    {'nome': 'Pedro', 'pai': 'Lucas'},
    {'nome': 'João', 'pai': 'Pedro'},
] 


def test():
    assert herdeiros(Familia) == 'Eduardo -> Lucas -> Pedro -> João' 
    print("OK")


if __name__ == '__main__':
    test()
