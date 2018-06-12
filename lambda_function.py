import sys
import logging
import pymysql
import os
#rds settings
rds_host  = "mydbinstance.c2ufqyoeq3be.us-east-1.rds.amazonaws.com"
name = "aditya"
password = "aditya2018"
db_name = "punchhDB"
table_name = 'punchh'
test_varialbe = os.environ(['TEST_VAR'])


logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=10)
except:
    logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    sys.exit()

logger.info("SUCCESS: Connection to RDS mysql instance succeeded")
def handler(event, context):
    """
    This function fetches content from mysql RDS instance
    """


    with conn.cursor() as cur:
        # cur.execute("create table %s ( EmpID  int NOT NULL, Name varchar(255) NOT NULL, PRIMARY KEY (EmpID))" % (table_name))
        # cur.execute('insert into %s (EmpID, Name) values(1, "Punchh1")'% (table_name))
        # cur.execute('insert into %s (EmpID, Name) values(2, "punchh2")'% (table_name))
        # cur.execute('insert into %s (EmpID, Name) values(3, "punchh3")'% (table_name))
        # conn.commit()
        # cur.execute("select * from %s"% (table_name))
        cur.execute("select count(*) from %s" %(table_name))
        for row in cur:
            print(row)
    return test_varialbe
