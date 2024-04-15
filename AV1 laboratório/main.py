from database import Database
from MotoristaCLI import MotoristaCLI
from MotoristaDAO import MotoristaDAO

db = Database(database="AV1lab", collection="Motoristas")

motorista_dao = MotoristaDAO(db.collection)

motorista_cli = MotoristaCLI(motorista_dao)

motorista_cli.run()