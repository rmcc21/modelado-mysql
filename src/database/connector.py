class Connector:
    def __init__(self, host, user, password, database) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database= database
    def connect(self) -> bool:
        pass
    def disconnect(self) -> bool:
        pass
    def executeQuery(self,sql):
        pass
    def executeSentence(self,sql,values):
        pass
