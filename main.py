from sqlalchemy import select,desc,func
from database import engine, LocalSession
from models import Base,User



Base.metadata.create_all(engine)


def insert_user():
    try:
        with LocalSession() as session:
            
            username = input("Username: ")
            full_name = input('full_name: ')
            age = int(input('age: '))
            email = input('email: ')
            year_of_birth = int(input('year_of_birth: '))
            
            print(type(User))
            
            user = User(
                full_name=full_name,
                username=username,
                age=age, 
                email=email, 
                year_of_birth=year_of_birth
            )
            
            session.add(user)
            session.commit()
        
        
    except ValueError as v:
        print("Malumotlar xato uzgartirishlar kiriritlmadi: ")
        session.rollback()
        
    finally :
        session.close()
    
def update_user():
    

    with LocalSession() as session:
        
        user = session.query(User).filter(User.id == 2).first()
        
        
        if user:
            user.username = "SHOOO"
            user.full_name = "SHOX"
            
            session.commit()
      
def delete_user():
     with LocalSession() as session:
         
        user = session.query(User).filter(User.id == 2).first()
         
        if user:
             session.delete(user)
             print(f"{user.id} User O'chirilidi") 
             session.commit() 
             
        else:
            print(f"Bunday User yuq")

def get_user():
    
    with LocalSession() as session:
        
        query = session.query(User).order_by(User.username).all()
        
        for _ in query:
            print(_.id,_.username)
     
def user_filter():
    """__sumary__
    18 yoshdan katta userlarni olib kelish sorting buyicha kamayish.
    """
    
    with LocalSession() as session:
        
        stmt = select(User).where(User.age > 18).order_by(User.age.desc())
        
        
        users = session.execute(stmt).scalars().all()
        
        for user in users:
            print(user.age, user.full_name)
                  
def email_filter():
    """_summary_
    gmail.com ishlatadigan userlarni topish
    """
  
    
    with LocalSession() as session:
        
        stmt = select(User).where(User.full_name.ilike("%tube.com"))
        
        users = session.scalars(stmt).all()
        if users:
            
            for user in users:
                print(user.id,user.full_name,user.email)
                
        else:
            print("%tube.com yuq ")
                
def big_user():
    """_summary_
    Eng katta yoshdagi 5 ta userni topish.
    """
    
    with LocalSession() as session:
        
        stmt = select(User).order_by(User.age.desc()).limit(5)  
        
        users = session.scalars(stmt) 
        
        for user in users:
            print(user.full_name,user.age)
        
def avarage():
    """_summary_
    Userlarning o‘rtacha yoshini hisoblash.
    """
    stmt = select(func.avg(User.age))
    
    with LocalSession() as session:
        
        result = session.scalar(stmt)
        
        
        print(f"Avarage result {result}")

            
def gender_count():
    """_summary_
    Har bir gender bo‘yicha userlar sonini chiqarish.
    """
    Male = "Male"
    Female = "Female"
    
    gender_list = []
    
    with LocalSession() as session:
        
        stmt = select(User)
        
        users = session.scalars(stmt).all()
        
        for user in users:
            
            gender_list.append(user.gender)
            
        print(f"MAle: {gender_list.count(Male)}\nFemale: {gender_list.count(Female)}")

def year_of_birth():
    """_summary_
    Qaysi tug‘ilgan yil eng ko‘p userga ega ekanini topish.
    """
    
    with LocalSession() as session:
        
        stmt = select(User.year_of_birth,func.count(User.id).label("user_count")).group_by(User.year_of_birth).order_by(func.count(User.id).desc().limit(1))
        
        result = session.execute(stmt).first()
        
        year, count = result

        print(f"Eng ko‘p user tug‘ilgan yil: {year}")
        print(f"Userlar soni: {count}")


def query():
    """
    Docstring for query
    50 ta userdan faqat: id, full_name
    ni olib keladigan query yozish.
    """
    with LocalSession() as session:
        
        stmt = select(User.id,User.full_name).limit(50)
        
        users = session.execute(stmt).all()
        
        for user in users:
            print(user.id,user.full_name)
        
        
        

query()
    