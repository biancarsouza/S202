class Professor:
    def __init__(self, nome):
        self.nome = nome
    
    def ministrar_aula(self, assunto):
        print(f'O professor {self.nome} está ministrando uma aula sobre {assunto}.')
        
        
class Aluno:
    def __init__(self, nome):
        self.nome = nome
    
    def presenca(self):
        print(f'O aluno {self.nome} está presente.')
              
            
class Aula:
    def __init__(self,professor, assunto):
        self.assunto = assunto
        self.professor = professor
        self.alunos = []   
        
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_presenca(self):
        print(f'Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:')
        for aluno in self.alunos:
            aluno.presenca()
            

professor = Professor("Jonas")
aluno1 = Aluno("Leonardo")
aluno2 = Aluno("Francisco")
aula = Aula(professor, "Banco de dados II")

aula.professor.ministrar_aula(aula.assunto)
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
aula.listar_presenca()