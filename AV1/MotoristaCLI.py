from UML import Motorista, Corrida, Passageiro

class MotoristaCLI:
    def __init__(self, motorista_model):
        self.motorista_model = motorista_model
        
    def create_motorista(self):
        corridas = self.create_corridas()

        nota = input("Nota do motorista: ")
        motorista = Motorista(nota, corridas)

        self.motorista_model.create_motorista(motorista.to_dict())

        
    def create_passageiro(self):
        nome = input("Nome do passageiro: ")
        documento = input("Documento do passageiro: ")
        passageiro = Passageiro(nome, documento)

        return passageiro

    def create_corridas(self):
        corridas = []

        while True:
            passageiro = self.create_passageiro()

            nota = int(input("Nota da corrida: "))
            distancia = float(input("Distância percorrida: "))
            valor = float(input("Valor da corrida: "))
            corrida = Corrida(nota, distancia, valor, passageiro)

            corridas.append(corrida)

            adicionar_outra = input("Inserir informações sobre uma nova corrida? (s/n): ")
            if adicionar_outra.lower() != "s":
                break

        return corridas

    def read_motorista(self):
        id = input("ID do motorista: ")
        self.motorista_model.read_motorista(id)

    def update_motorista(self):
        id = input("ID do motorista: ")

        corridas = self.create_corridas()

        nota = input("Nota do motorista: ")
        motorista = Motorista(nota, corridas)

        self.motorista_model.update_motorista(id, motorista.to_dict())

    def delete_motorista(self):
        id = input("ID do motorista: ")

        self.motorista_model.delete_motorista(id)

    def menu(self):
        print("Menu")
        print("1 - Criar motorista")
        print("2 - Ler as informações de um motorista")
        print("3 - Atualizar as informações de um motorista")
        print("4 - Deletar um motorista")
        print("5 - Sair do menu\n")

    def run(self):
        while True:
            self.menu()
            
            opcao = input("Escolha uma opção: ")
            print("\n")

            if opcao == "1":
                self.create_motorista()
            elif opcao == "2":
                self.read_motorista()
            elif opcao == "3":
                self.update_motorista()
            elif opcao == "4":
                self.delete_motorista()
            elif opcao == "5":
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida. Insira outra de acordo com o menu.")

            print("\n")
