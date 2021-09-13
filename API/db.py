from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


# from credentials import connection
# from sqlalchemy import create_engine, text
# from sqlalchemy.ext.declarative import declarative_base

#This will create the connection to the MySQL AWS RDS Instance
# engine = create_engine(connection)
# #This 
# Base = declarative_base(engine)
# Base.metadata.reflect(engine)

# with engine.connect() as conn:
#     result = conn.execute(text("select * from DallasPermits.permits"))
#     for row in result:
#         print(f'permit_id: {row[1]}, issuedDate: {row[2]}')