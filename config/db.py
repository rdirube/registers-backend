from sqlalchemy import create_engine, MetaData


engine = create_engine("mysql+pymysql://zinu:password@localhost:3306/permits")

meta = MetaData()

conn = engine.connect()