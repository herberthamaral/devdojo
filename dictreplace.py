#-*- coding: utf-8 -*-
import unittest

def replacer(string,dicionario):
    
    chaves = dicionario.keys()
    
    if string == "":
        return ""
    
    for chave in chaves:
        string = string.replace("$%s$"%chave, dicionario[chave])
    
    return string

def replacer_comprehension(string,dicionario):
    if dicionario.__len__() == 0:
        return string
    return [string.replace("$%s$"%key,dicionario[key]) for key in dicionario.keys()][0]
    
replacer = replacer_comprehension

class TestDictReplace(unittest.TestCase):
    
    def testSeEntradaForStringVazia_DeveRetornarStringVazia(self):
        assert replacer("",{}) == ""
    
    def testSeEntradaForStringVaziaEDicionarioComValor_RetornaStringVazia(self):
        assert replacer("",{'a':'b'}) == ""
    
    def testSeStringSemToken_RetornaString(self):
        valor = "eu sou uma string sem token"
        assert replacer(valor,{}) == valor

    def testSeStringSemToken_DicionarioComValor_RetornaString(self):
        valor = "eu sou uma outra string"
        assert replacer(valor, { 'a': 'a' }) == valor
        
    def testSeStringTemToken_DicionarioComValor_RetornaStringComReplace(self):
        valor = "Olá $name$"
        assert replacer(valor, {'name':'Glauco'}) == "Olá Glauco"
        
    def testSeStringTemToken_DicionarioComMultiplosValores_RetornaStringComReplace(self):
        valor = "Olá $name$, bem vindo ao $lugar$"
        assert replacer(valor, {'name': 'Glauco', 'lugar':'DevDojo'}) == "Olá Glauco, bem vindo ao DevDojo"
        
        
    def testSeStringTemTokenRepetido_DicionarioComValor_RetornaStringComReplaceCompleto(self):
        valor = "Olá $name$, você é mesmo o $name$, ou está me enganando!"
        assert replacer(valor, {'name' : 'Glauco'}) == "Olá Glauco, você é mesmo o Glauco, ou está me enganando!"
        
    def testSeStringTemToken_DicionarioNaoTemChaveCorrespondente_RetornaStringSemSubstituirChave(self):
        valor = "Olá $name$ seja bem vindo ao $local$"
        self.assertEquals( replacer(valor, { 'name' : 'Glauco' }) , "Olá Glauco seja bem vindo ao $local$")
        
    
        
if __name__ == '__main__':
    unittest.main()
