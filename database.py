from sqlalchemy import create_engine,URL
from sqlalchemy.orm import sessionmaker

from config import USER,NAME,PASS,PORT,HOST


DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=USER,
    password=PASS,
    database=NAME,
    port=PORT,
    host=HOST,
)

engine = create_engine(DATABASE_URL)

LocalSession = sessionmaker(bind=engine)  # class factory yaratib beradi   session = LocalSession() -> Bu real  INSCTANCE yaratadi



