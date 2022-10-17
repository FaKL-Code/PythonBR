from validate_docbr import CPF

class Cpf:
    
    def __init__(self, documento):
        if self.cpf_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("Cpf invalido")
        
    def __str__(self):
        return self.formatar_cpf()
    
    def cpf_valido(self, documento):
        if len(documento) == 11:
            validador = CPF()
            return validador.validate(documento)
        else:
            return False
        
    def formatar_cpf(self):
        
        mascara = CPF()

        return mascara.mask(self.cpf)