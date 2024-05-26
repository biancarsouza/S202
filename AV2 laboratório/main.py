from teacher_crud import TeacherCRUD
from database import Database

db = Database("bolt://34.207.191.185:7687", "neo4j", "upside-boil-retractor")
crud = TeacherCRUD(db)

option = 0

while option != 5:
    print("1 - Criar um professor")
    print("2 - Buscar um professor")
    print("3 - Deletar um professor com base no nome")
    print("4 - Atualizar o CPF de um professor com base no nome")
    print("5 - Sair\n")
    
    try:
        option = int(input("Selecione uma opção: "))
    
    except ValueError:
        print("Opção inválida, insira outra de acordo com o menu.\n")
        continue

    print();
    
    if option == 1:
        name = input("Nome: ")

        try:
            ano_nasc = int(input("Ano de nascimento: "))

        except ValueError:
            print("Ano inválido, insira outro valor.")
            continue
        
        cpf = input("CPF: ")

        crud.createTeacher(name, ano_nasc, cpf)

        print("\nProfessor criado.\n")

    elif option == 2:
        name = input("Nome do professor buscado: ")
        teacher = crud.readTeacher(name)

        print();

        if teacher:
            print("Professor encontrado!")
            print(f'Nome: {teacher[0]["t.name"]}.\nAno de nascimento: {teacher[0]["t.ano_nasc"]}.\nCPF: {teacher[0]["t.cpf"]}.')
        
        else:
            print("O professor não foi encontrado.")
        
        print();
    
    elif option == 3:
        name = input("Nome do professor deletado: ")
        print();
        crud.deleteTeacher(name)
        print("Professor deletado.\n");
    
    elif option == 4:
        name = input("Nome do professor cujo CPF será alterado: ")
        new_cpf = input("Novo CPF: ")

        print();

        crud.updateTeacher(name, new_cpf)

        print("CPF atualizado.\n")
    
    elif option == 5:
        db.close()
        print("Conexão com o banco de dados fechada.")
    
    else:
        print("Opção inválida, insira outra de acordo com o menu.\n")