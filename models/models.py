from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

registers_table = Table("operations_log", meta, Column("id", Integer, primary_key=True),
                    Column("adress", String(255)), Column("amount", String(100)), 
                    Column("operation", String(50)), Column ("creation_time", String(100)))


meta.create_all(engine)