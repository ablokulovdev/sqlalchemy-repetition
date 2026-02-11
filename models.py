import enum
from sqlalchemy import(
    Column,
    String,
    Integer,
    Enum,
    BigInteger
    
)
from sqlalchemy.orm  import DeclarativeBase


class Base(DeclarativeBase):
    pass

class Ganre(enum.Enum):
    MALE = "MALE"
    WOMAN = "WOMAN"
    


class User(Base):
    
    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True)
    full_name = Column(String(length=50),nullable=False,index=True)
    age = Column(Integer,nullable=False)
    email = Column(String(length=50),index=True)
    ganre = Column(Enum(Ganre))
    year_of_birth = Column(BigInteger,nullable=False)

