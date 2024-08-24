import pymysql

db_host = "inst-db-cym.cdk4wc4o04z5.us-east-1.rds.amazonaws.com"
db_user = "jonier"
db_password = "12345678"
db_database = "db_users"

def connectionSQL(): 
    try: 
        connection = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database
        )
        print("Succesfull connection to database")
        return connection
    except Exception as err:
        print("Error connecting to database:", err)
        return None

def add_user(ident, name, lastname, birthday):
    instruction = "INSERT INTO users VALUES ("+ident+", '"+name+"', '"+lastname+"', '"+birthday+"')"
    connection = connectionSQL()
    cursor = connection.cursor()
    try:
        cursor.execute(instruction)
        connection.commit()
        print("User added")
    except Exception as err:
        print("Error when adding the user", err)
    return True

def consult_user(ident):
    instruction = "SELECT * FROM users WHERE id =" + ident
    connection = connectionSQL()
    cursor = connection.cursor()
    try:
        cursor.execute(instruction)
        result_data = cursor.fetchall()
        return result_data
    except Exception as err:
        print("Error consulting the user", err)
        return False