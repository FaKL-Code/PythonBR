from validate_docbr import CNPJ

class Cnpj:
    
    def __init__(self, documento):
        if self.cnpj_valido(documento):
            self.cnpj = documento
        else:
            raise ValueError("cnpj invalido")
        
    def __str__(self):
        return self.formatar_cnpj()
    
    def cnpj_valido(self, documento):
        if len(documento) == 14:
            validador = CNPJ()
            return validador.validate(documento)
        else:
            return False
        
    def formatar_cnpj(self):
        
        mascara = CNPJ()

        return mascara.mask(self.cnpj)