from database import Database
from gamedatabase import gamedatabase

db = Database("bolt://44.199.217.21:7687", "neo4j", "checkpoints-candidate-notes")

game_db = gamedatabase(db)

def createPlayer():
    name = input("Nome: ")
    game_db.createPlayer(name)

    print(f"\nO player '{name}' foi criado com sucesso!")

def readPlayers():
    players = game_db.getPlayers()

    print("\n")

    if players:
        print("players: ")
        for player in players:
            print(player["name"])
    else:
        print("Não há players cadastrados.")

def updatePlayer():
    player_id = int(input("Digite o id do player a ser atualizado: "))
    new_name = input("Digite o novo nome do player: ")
    game_db.updatePlayer(player_id, new_name)

    print(f"\nO nome do player (id: {player_id} foi atualizado para '{new_name}'.")

def deletePlayer():
    player_id = int(input("Digite o id do player que será excluído: "))
    game_db.deletePlayer(player_id)

    print(f"\nO player (id: {player_id}) foi excluído com sucesso!\n")

def createMatch():
    players = input("Digite os nomes dos players separados por vírgula: ").split(",")
    result = input("Digite o resultado da partida: ")
    game_db.createMatch(players, result)

    print("\nA partida foi registrada com sucesso!")

def deleteMatch():
    match_id = int(input("Digite o id da partida a ser excluída: "))
    game_db.deleteMatch(match_id)

    print(f"\nA partida (id: {match_id}) foi excluída com sucesso!")

def getMatches():
    matches = game_db.getMatches()

    print("\n")

    if matches:
        print("Partidas registradas:")
        for match in matches:
            print(f"id: {match['match_id']}, resultado: {match['result']}")
    else:
        print("Não há partidas registradas.")

def getPlayerMatches():
    player_id = int(input("Digite o id do player para obter seu histórico de partidas: "))
    matches = game_db.getPlayerMatches(player_id)

    print("\n")

    if matches:
        print(f"Histórico de partidas do player (id: {player_id}): ")
        for match in matches:
            print(f"id da partida: {match['match_id']}, resultado: {match['result']}")
    else:
        print(f"O player (id: {player_id}) não possui histórico de partidas.")

def closeConnection():
    db.close()

    print("\nConexão com o banco de dados fechada.")


while True:
    print("\nSelecione uma opção: ")
    print("1 - Criar um player")
    print("2 - Listar os players criados")
    print("3 - Atualizar um player")
    print("4 - Excluir um player")
    print("5 - Registrar uma partida")
    print("6 - Excluir uma partida")
    print("7 - Listar as partidas registradas")
    print("8 - Histórico de partidas de um player")
    print("9 - Fechar conexão com o banco de dados")
    print("10 - Encerrar o programa\n")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        createPlayer()
    elif escolha == "2":
        readPlayers()
    elif escolha == "3":
        updatePlayer()
    elif escolha == "4":
        deletePlayer()
    elif escolha == "5":
        createMatch()
    elif escolha == "6":
        deleteMatch()
    elif escolha == "7":
        getMatches()
    elif escolha == "8":
        getPlayerMatches()
    elif escolha == "9":
        closeConnection()
        break
    elif escolha == "10":
        print("\nEncerrado.")
        break
    else:
        print("Opção inválida, insira outra opção de acordo com o menu.\n")