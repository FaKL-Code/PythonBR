from operator import truediv


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
            return True
        else:
            return False
        
    def formatar_cpf(self):
        
        self.parte_um = self.cpf[:3]
        self.parte_dois = self.cpf[3:6]
        self.parte_tres = self.cpf[6:9]
        self.parte_quatro = self.cpf[9:]

        return f'{self.parte_um}.{self.parte_dois}.{self.parte_tres}-{self.parte_quatro}'