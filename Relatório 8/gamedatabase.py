class gamedatabase:
    def __init__(self, database):
        self.db = database

    def createPlayer(self, name):
        query = "CREATE (:Player {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def updatePlayer(self, player_id, new_name):
        query = "MATCH (p:Player) WHERE id(p) = $player_id SET p.name = $new_name"
        parameters = {"player_id": player_id, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def deletePlayer(self, player_id):
        query = "MATCH (p:Player) WHERE id(p) = $player_id DETACH DELETE p"
        parameters = {"player_id": player_id}
        self.db.execute_query(query, parameters)

    def createMatch(self, players, result=None):
        query = (
            "CREATE (m:Match {result: $result})"
            "WITH m "
            "UNWIND $players AS player_name "
            "MATCH (p:Player {name: player_name}) "
            "MERGE (p)-[:PARTICIPATED_IN]->(m)"
        )
        parameters = {"result": result, "players": players}
        self.db.execute_query(query, parameters)

    def deleteMatch(self, match_id):
        query = "MATCH (m:Match) WHERE id(m) = $match_id DETACH DELETE m"
        parameters = {"match_id": match_id}
        self.db.execute_query(query, parameters)

    def getPlayers(self):
        query = "MATCH (p:Player) RETURN p.name AS name, id(p) AS id"
        results = self.db.execute_query(query)
        return [{"id": result["id"], "name": result["name"]} for result in results]

    def getMatches(self):
        query = "MATCH (m:Match) RETURN id(m) AS match_id, m.result AS result"
        results = self.db.execute_query(query)
        return [{"match_id": result["match_id"], "result": result["result"]} for result in results]

    def getPlayerMatches(self, player_id):
        query = (
            "MATCH (p:Player)-[:PARTICIPATED_IN]->(m:Match) "
            "WHERE id(p) = $player_id "
            "RETURN id(m) AS match_id, m.result AS result"
        )
        parameters = {"player_id": player_id}
        results = self.db.execute_query(query, parameters)
        return [{"match_id": result["match_id"], "result": result["result"]} for result in results]