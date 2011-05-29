#-*- coding: utf-8 -*-

class HelloPython(object):
    """Classe de exemplo para a galera do #DevDojo com exemplos de 
    docstrings, estruturas de controle, métodos, doctests e algumas
    cositas mas ;-)"""
    
    x = 0
    def __init__(self):
        self.x = 1

    def flipflop(self,number):
        """Retorna flip, caso number seja divisivel por 3
        retorna flop caso number seja divisivel por 5.
        retorna o numero em caso contrario
        Exemplo de uso:

        >>> hello = HelloPython()
        >>> hello.flipflop(1)
        1
        >>> hello.flipflop(3)
        'flip'
        >>> hello.flipflop(6)
        'flip'
        >>> hello.flipflop(10)
        'flop'

        O algoritmo precisa retornar flipflop caso o numero seja divisivel por 3 e por 5 ao mesmo tempo

        >>> hello.flipflop(15)
        'flipflop'
        """
        
        retorno = ''
        if number % 3 == 0:
            retorno = 'flip'
        if number %5 == 0:
            retorno += 'flop'

        if len(retorno) > 0:
            return retorno

        return number 

if __name__=='__main__':
    import doctest
    doctest.testmod()
