from abc import ABC, abstractmethod

class DatabaseConnector(ABC):
	@abstractmethod
	def connect(self):
		pass

	@abstractmethod
	def execute_query(self, query):
		pass

class MySQLConnector(DatabaseConnector):
	def connect(self):
		print("Connecting to MySQL database..")

	def execute_query(self, query):
		print(f"MySQL executing query: {query}")

class PostgresConnector(DatabaseConnector):
	def connect(self):
		print("Connecting to PostgresSQL database..")

	def execute_query(self, query):
		print(f"PostgresSQL executing query: {query}")

def run_query(db: DatabaseConnector, query: str):
	db.connect()
	db.execute_query(query)

if __name__ == '__main__':
	mysql = PostgresConnector()
	post = MySQLConnector()

	run_query(mysql, "SELECT * FROM users;")
	run_query(post, "SELECT * FROM orders;")