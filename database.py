import sqlalchemy as sql
import sqlalchemy.ext.declarative as dec
import sqlalchemy.orm as orm

DATABASE_URL = "postgresql://myuser:password@localhost/question_database"

engine = sql.create_engine(DATABASE_URL)

session_local = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = dec.declarative_base()
