from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Member(Base):
    __tablename__ = 'member'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    inscription_date = Column(String(250)) #DD/MM/YY
    picture = Column(String(250), default="blank_user.gif")

class Machine(Base):
    __tablename__ = 'machine'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    machine_type = Column(String(250), nullable=False)
    company = Column(String(250))
    description = Column(String(250))
    quantity = Column(Integer)
    picture = Column(String(250), default="blank_machine.gif")
    price = Column(Integer) # euros

class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    description = Column(String(250))
    picture = Column(String(250), default="blank_project.gif")
    source = Column(String(850))
    end_date = Column(String(10)) #DD/MM/YY
    member_id = Column(Integer, ForeignKey('member.id'))
    member = relationship(Member)

class Tag(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    tag_name = Column(String(100), nullable=False)
    project_id = Column(Integer, ForeignKey('project.id'))
    project = relationship(Project)

engine = create_engine('sqlite:///lepetitfablabdeparis.db', encoding='utf-8')
Base.metadata.create_all(engine)
