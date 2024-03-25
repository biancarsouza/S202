from pymongo import MongoClient

client = MongoClient('mongodb+srv://biancaribeiro:BOGQX8IStVU5Xurg@cluster0.cel6uzr.mongodb.net/')
db = client["rel5"]
collection = db["Livros"]

def menu():
    print("1 - Adicionar livro")
    print("2 - Listar todos os livros")
    print("3 - Atualizar livro")
    print("4 - Remover livro")
    print("5 - Sair")

def create():
    _id = input("Digite o id do livro: ")
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = int(input("Digite o ano do livro: "))
    preco = float(input("Digite o preço do livro: "))

    livro = {"_id": _id, "titulo": titulo, "autor": autor, "ano": ano, "preco": preco}
    collection.insert_one(livro)

    print("O livro foi adicionado ao banco de dados com sucesso!\n")

def update():
    _id = input("Digite o id do livro que deseja atualizar: ")
    livro = collection.find_one({"_id": _id})
    if livro:
        titulo = input("Digite o novo título do livro (ou enter para manter o atual): ")
        autor = input("Digite o novo autor do livro (ou enter para manter o atual): ")
        ano = input("Digite o novo ano do livro (ou enter para manter o atual): ")
        preco = input("Digite o novo preço do livro (ou enter para manter o atual): ")
        update_data = {}

        if titulo:
            update_data["titulo"] = titulo

        if autor:
            update_data["autor"] = autor

        if ano:
            update_data["ano"] = int(ano)

        if preco:
            update_data["preco"] = float(preco)

        collection.update_one({"_id": _id}, {"$set": update_data})
        print("Livro atualizado com sucesso!\n")

    else:
        print("O livro não foi encontrado.\n")

def delete():
    _id = input("Digite o id do livro que deseja remover do banco de dados: ")
    result = collection.delete_one({"_id": _id})

    if result.deleted_count:
        print("O livro foi removido com sucesso!\n")
    else:
        print("O livro não foi encontrado.\n")

def read():
    livros = collection.find()
    print("\nLista de livros:\n")
    for livro in livros:
        print(f"Id: {livro["_id"]}")
        print(f"Título: {livro["titulo"]}")
        print(f"Autor: {livro["autor"]}")
        print(f"Ano: {livro["ano"]}")
        print(f"Preço: {livro["preco"]}\n")
        print("---------------------------------\n")

while True:
    menu()
    opcao = input("\nEscolha uma opção: ")
    print("\n")

    if opcao == "1":
        create()
    elif opcao == "2":
        read()
    elif opcao == "3":
        update()
    elif opcao == "4":
        delete()
    elif opcao == "5":
        print("\nSaindo do menu.")
        break
    else:
        print("\nOpção inválida. Tente novamente.\n")