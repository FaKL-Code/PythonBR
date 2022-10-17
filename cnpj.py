from validate_docbr import CNPJ

class Cnpj:
    
    def __init__(self, documento):
        if self.cnpj_valido(documento):
            self.cnpj = documento
        else:
            raise ValueError("cnpj invalido")
        
    def __str__(self):
        return self.formatar()
    
    def cnpj_valido(self, documento):
            validador = CNPJ()
            return validador.validate(documento)
        
    def formatar(self):
        
        mascara = CNPJ()

        return mascara.mask(self.cnpj)