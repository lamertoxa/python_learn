# import sqlalchemy
# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///library.db',echo=True)
# from sqlalchemy import Table, Column, Integer,String,MetaData,ForeignKey,text
#
# metadata = MetaData(bind=engine)
#
#
#  Column('name', String(50)) is possible
#
#
# USERS_TABLE = metadata.tables['customers']
#
#  insert_stmt.execute(name='Alexandre Dumas') # insert a single entry
#  insert_stmt.execute([{'name': 'Mr X'}, {'name': 'Mr Y'}]) # a list of entries
#  metadata.bind = engine # no need to explicitly bind the engine from now on
#  select_stmt = authors_table.select(authors_table.c.id==2)
#  result = select_stmt.execute()
#  result.fetchall()
#  del_stmt = authors_table.delete()
#  del_stmt.execute(whereclause=text("name='Mr Y'"))
#  del_stmt.execute()