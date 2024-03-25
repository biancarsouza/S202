from pymongo import MongoClient

client = MongoClient('mongodb+srv://biancaribeiro:BOGQX8IStVU5Xurg@cluster0.cel6uzr.mongodb.net/')
db = client["rel2"]
collection = db["Aula"]


class Professor:
    def __init__(self, nome):
        self.nome = nome
        
        
class Aluno:
    def __init__(self, nome):
        self.nome = nome
              

class Aula:
    def __init__(self, professor, assunto, alunos=None):
        self.assunto = assunto
        self.professor = professor
        if alunos is None:
            self.alunos = []
        else:
            self.alunos = alunos
            
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
        
    def salvar_no_banco(self):
        if len(self.alunos) >= 4:  # Verifica se há pelo menos 4 alunos
            data = {
                "assunto": self.assunto,
                "professor": self.professor.nome,
                "alunos": [aluno.nome for aluno in self.alunos]
            }
            collection.insert_one(data)
            print(f"Aula do professor {self.professor.nome} foi salva no banco de dados.")
        else:
            print(f"Não foi possível salvar a aula do professor {self.professor.nome} no banco de dados. É necessário pelo menos 4 alunos.")



professor1 = Professor("Jonas")
professor2 = Professor("Chris")
professor3 = Professor("Ynoguti")
professor4 = Professor("Karina")

aluno1 = Aluno("Leonardo")
aluno2 = Aluno("Francisco")
aluno3 = Aluno("Arthur")
aluno4 = Aluno("Diego")
aluno5 = Aluno("Bianca")

aula1 = Aula(professor1, "Banco de dados II", [aluno1, aluno2, aluno3, aluno4])
aula1.salvar_no_banco()
aula2 = Aula(professor2, "Programação orientada a objetos", [aluno4, aluno2, aluno3, aluno1])
aula2.salvar_no_banco()
aula3 = Aula(professor3, "Algoritmos I", [aluno5, aluno2, aluno3, aluno1])
aula3.salvar_no_banco()
aula4 = Aula(professor4, "Física II", [aluno2, aluno5, aluno4])
aula4.salvar_no_banco()