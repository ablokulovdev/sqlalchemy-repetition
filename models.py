
import enum
from datetime import datetime
from sqlalchemy import(
    Column,
    String,
    Integer,
    Enum,
    BigInteger,
    DateTime
    
)
from sqlalchemy.orm  import DeclarativeBase


class Base(DeclarativeBase):
    pass

    

class User(Base):    
    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True)
    full_name = Column(String(length=50),nullable=False,index=True)
    username =  Column(String(length=50),nullable=False,index=True)
    age = Column(Integer,nullable=False)
    email = Column(String(length=50),index=True)
    gender = Column(String(length=50), nullable=False)
    year_of_birth = Column(BigInteger,nullable=False)
    
    created_at = Column(DateTime,default=datetime.utcnow())
    updated_at = Column(DateTime,onupdate=datetime.utcnow())

