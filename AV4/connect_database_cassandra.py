from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import json

cloud_config= {
  'secure_connect_bundle': 'Teoria/AV4/secure-connect-estoque.zip'
}

with open("Teoria/AV4/Estoque-token.json") as f:
    secrets = json.load(f)
    
CLIENT_ID = secrets["clientId"]
CLIENT_SECRET = secrets["secret"]

auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
  print(row[0])
else:
  print("An error occurred.")

session.set_keyspace('estoque')

input = input("Digite o nome do carro: ")

result = session.execute(f'SELECT nome, estante, quantidade FROM estoque WHERE carro = \'{input}\' ALLOW FILTERING;').all()

if result is not None:
    for r in result:
        print(r)