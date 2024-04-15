from database import Database
from bson.objectid import ObjectId

class MotoristaDAO:
    def __init__(self, db: Database):
        self.db = db

    def create_motorista(self, motorista_data: dict):
        try:
            result = self.db.collection.insert_one(motorista_data)
            print(f"Motorista criado com sucesso! Seu ID é: {result.inserted_id}.")
            return result.inserted_id
        except Exception as e:
            print(f"Erro ao criar motorista: {e}.")
            return None

    def read_motorista(self, motorista_id: str):
        try:
            motorista = self.db.collection.find_one({"_id": ObjectId(motorista_id)})

            if motorista:
                print("O motorista foi encontrado!")
                print(f"ID: {motorista['_id']}")
                print(f"Nota do motorista: {motorista.get('nota')}\n")
                print("Corridas:")
                print("------------------------------------")

                for corrida in motorista.get('corridas', []):
                    print(f"Nota: {corrida.get('nota')}")
                    print(f"Distância: {corrida.get('distancia')} km")
                    print(f"Valor: R$ {corrida.get('valor')}")

                    passageiro = corrida.get('passageiro')

                    if passageiro:
                        print("\nInformações sobre o passageiro:")
                        print(f"Nome: {passageiro.get('nome')}")
                        print(f"Documento: {passageiro.get('documento')}")
                    else:
                        print("Passageiro não encontrado.")
                    
                    print("------------------------------------")
            else:
                print("O motorista não foi encontrado.")
        except Exception as e:
            print(f"Erro ao procurar o motorista: {e}.")

    def update_motorista(self, motorista_id: str, motorista_data: dict):
        try:
            result = self.db.collection.update_one({"_id": ObjectId(motorista_id)}, {"$set": motorista_data})
            print(f"As informações do motorista foram atualizadas! {result.modified_count} documento(s) modificado(s).")
            return result.modified_count
        except Exception as e:
            print(f"Erro ao atualizar as informações do motorista: {e}.")
            return None

    def delete_motorista(self, motorista_id: str):
        try:
            motorista_id_obj = ObjectId(motorista_id)
            result = self.db.collection.delete_one({"_id": motorista_id_obj})

            if result.deleted_count > 0:
                print(f"O motorista foi deletado. {result.deleted_count} documento(s) deletado(s).")
            else:
                print("Nenhum motorista foi deletado.")
            
            return result.deleted_count
        except Exception as e:
            print(f"Erro ao deletar o motorista: {e}.")
            return None
