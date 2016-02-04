'''
Created on Mar 26, 2015

@author: raffccc
'''

class Pessoa(object):
    '''
    Representa uma pessoa
    '''


    def __init__(self, idade=0, nome=''):
        '''
        Constructor
        '''
        self.idade = idade
        self.nome = nome
        
    def peidar(self):
        print 'BUFFFFFFFFFfffff'
        
    def descricao(self):
        print self.nome, self.idade