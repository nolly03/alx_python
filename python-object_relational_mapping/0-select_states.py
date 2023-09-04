#Get all states 
import MySQLdb
class get_states:
    def __init__(self, username, password, database_name):
        self.name = username
        self.password = password
        self.database_name = database_name
        
db_connect = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='tester',
    passwd='password'
    db='hbtn_0e_0_usa'
)

states = db_connect.cursor()
cities = cursor.execute(
    "
    CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
    USE hbtn_0e_0_usa;
    CREATE TABLE IF NOT EXISTS states (
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(256) NOT NULL,
        PRIMARY KEY (id)
        );
        INSERT INTO states (name) VALUES
        ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");"
)