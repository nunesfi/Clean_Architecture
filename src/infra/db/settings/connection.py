from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            'mysql+pymysql',
            'user1',
            'secret',
            'localhost',
            '3306',
            'clean_database'

        )
        self.__engine = self.__create_database_engine()
        self.session = None

    # Mecanismo para conexão ao Banco de dados
    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine
    
    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self
    
    def __exit__(self, exe_type, exe_val, exe_tb):
        self.session.close()