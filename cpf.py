from validate_docbr import CPF

class Cpf:
    
    def __init__(self, documento):
        if self.cpf_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("Cpf invalido")
        
    def __str__(self):
        return self.formatar()
    
    def cpf_valido(self, documento):
            validador = CPF()
            return validador.validate(documento)
        
    def formatar(self):
        
        mascara = CPF()

        return mascara.mask(self.cpf)