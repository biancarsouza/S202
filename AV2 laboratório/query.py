from database import Database
import random

db = Database("bolt://34.207.191.185:7687", "neo4j", "upside-boil-retractor")


class QueryHandler:
    def __init__(self, db):
        self.db = db

    # 1. A
    def getRenzo(self):
        query = "MATCH (t:Teacher {name: 'Renzo'}) RETURN t.ano_nasc, t.cpf"
        return self.db.execute_query(query)

    # 1. B
    def getLetterM(self):
        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name, t.cpf"
        return self.db.execute_query(query)

    # 1. C
    def getCities(self):
        query = "MATCH (c:City) RETURN c.name"
        return self.db.execute_query(query)

    # 1. D
    def getSchoolByNumber(self):
        query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name, s.address, s.number"
        return self.db.execute_query(query)

    # 2. A
    def getTeachersAge(self):
        query = "MATCH (t:Teacher) RETURN t.name, substring(t.name, 3, 1)"
        return self.db.execute_query(query)
    
    # 2. B
    def getCitiesPopulations(self):
        query = "MATCH (c:City) RETURN c.name, c.population"
        return self.db.execute_query(query)
    
    # 2. C
    def getModifyCitiesNames(self):
        query = "MATCH (c:City) WHERE c.cep = '37540-000' RETURN replace(c.name, 'a', 'A')"
        return self.db.execute_query(query)
    
    # 2. D
    def getThirdChar(self):
        query = "MATCH (t:Teacher) RETURN t.name, substring(t.name, 3, 1)"
        return self.db.execute_query(query)


query_handler = QueryHandler(db)

print("1. A")
result = query_handler.getRenzo()
print(f'Ano de nascimento: {result[0]["t.ano_nasc"]}.\nCPF: {result[0]["t.cpf"]}.')

print("\n1. B")
result = query_handler.getLetterM()
for item in result:
    print(f'Nome: {item["t.name"]}.\nCPF: {item["t.cpf"]}.\n')

print("1. C")
result = query_handler.getCities()
for item in result:
    print(f'Cidade: {item["c.name"]}.')

print("\n1. D")
result = query_handler.getSchoolByNumber()
for item in result:
    print(f'Nome: {item["s.name"]}.\nEndereço: {item["s.address"]}.\nNúmero: {item["s.number"]}.\n')

print("2. A")
result = query_handler.getTeachersAge()
for item in result:
    print(f'Nome: {item["t.name"]}.\nTerceira letra: {item["substring(t.name, 3, 1)"]}.\n')

print("2. B")
result = query_handler.getCitiesPopulations()
for item in result:
    print(f'Cidade: {item["c.name"]}.\nPopulação: {item["c.population"]}.\n')

print("2. C")
result = query_handler.getModifyCitiesNames()
for item in result:
    print('Cidade: {}.'.format(item["replace(c.name, 'a', 'A')"]))

print("\n2. D")
result = query_handler.getThirdChar()
for item in result:
    name = item["t.name"]
    if len(name) > 3:
        random_char = random.choice(name[3:])
        print(f'{name}: {random_char}.')