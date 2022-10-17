from documento import Documento
from telefones import Telefones

documento = input('Digite o documento -> ')

docs = Documento(documento)

print(docs.doc)

texto = input('Insira o numero de telefone -> ')

resposta = Telefones(texto)

print(resposta)