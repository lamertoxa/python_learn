import sqlalchemy
from sqlalchemy.sql import select, and_
from sqlalchemy import create_engine

engine = create_engine('sqlite:///q1.db')
from sqlalchemy import MetaData, Table, ForeignKey, text

metadata = MetaData(engine)
# MetaData.reflect(metadata)
customers = Table("Customers", metadata, autoload=True)
conn = engine.connect()

table = select([customers]).where(customers.c.Grade > 200)

result = conn.execute(table)
itter = result.fetchall()
print(f'Connected to SQLite\nTotal rows are:   {len(itter)}\nPrinting each row')

for row in itter:

    pass
    print(
          f"Id:  {row['Id']}\n"
          f"Name:  {row['Name']}\n"
          f"City: {row['City']}\n"
          f"Grade: {row['Grade']}\n"
          f"Seller: {row['salesperson_id']}\n\n")



print ('The SQLite connection is closed')
conn.close()
