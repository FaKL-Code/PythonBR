from cpf import Cpf
from cnpj import Cnpj

class Documento:
    
    def __init__(self, documento):
        self.doc = self.cria_documento(documento)
    
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return Cpf(documento)
        elif len(documento) == 14:
            return Cnpj(documento)
        else:
            raise ValueError('Documento invalido')