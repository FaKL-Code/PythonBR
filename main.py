from cpf import Cpf
from cnpj import Cnpj

tipo = input('Qual o tipo do documento a ser usado? -> 1 - CPF 2 - CNPJ ')
documento = input('Digite o documento -> ')

if tipo == '1':
    cpf = Cpf(documento)
    print(cpf)
elif tipo == '2':
    cnpj = Cnpj(documento)
    print(cnpj)
else:
    raise ValueError('Tipo de documento invalido')
