from neo4j import GraphDatabase
         
class DBFamily:
    
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def drop_all(self):
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")

    def get_siblings(self, nome):
        with self.driver.session() as session:
            results = session.run("MATCH (p:Pessoa)-[:IRMAO_DE]->(c:Pessoa {nome: $nome}) RETURN p", nome=nome)
            return [result['p']['nome'] for result in results]
        
    def get_owner(self, nome):
        with self.driver.session() as session:
            results = session.run("MATCH (p:Pessoa)-[:DONO_DE]->(c:Pet {nome: $nome}) RETURN p", nome=nome)
            return [result['p']['nome'] for result in results]
    
    def get_married(self, nome):
        with self.driver.session() as session:
            results = session.run("MATCH (p:Pessoa)-[r:CASADO_COM]->(c:Pessoa {nome: $nome})  RETURN p, r", nome=nome)
            return [(result['p']['nome'], result['r']['desde']) for result in results]
        

banco = DBFamily("bolt://54.159.99.16:7687", "neo4j", "range-advancement-realignments")

opcao = int(input("""1-Quem são os irmãos da Bianca?
2-Quem é dono da pipoca?
3-Com quem e desde quando Paulo é casado?
OPCÃO: """))
if opcao == 1:
    print("Irmãos da Bianca:")
    print(banco.get_siblings("Bianca"))
elif opcao == 2:
    print("Dono da pipoca:")
    print(banco.get_owner("Pipoca"))
elif opcao == 3:
    print("Esposa de Paulo e data do casamento:")
    print(banco.get_married("Paulo"))

banco.close()