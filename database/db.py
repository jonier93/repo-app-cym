import pymysql

db_host = "inst-db-cym.cdk4wc4o04z5.us-east-1.rds.amazonaws.com"
db_user = "jonier"
db_password = "12345678"
db_database = "db_users"

try: 
    pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_database
    )
    print("Succesfull connection to database")
except Exception as err:
    print("Error connecting to database:", err)