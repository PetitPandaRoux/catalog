from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from flask_login import LoginManager, UserMixin


from flask_dance.consumer.backend.sqla import OAuthConsumerMixin


Base = declarative_base()


class Member(Base, UserMixin):
    __tablename__ = 'member'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    inscription_date = Column(String(250))  # DD/MM/YY
    picture = Column(String(250), default="blank_user.gif")

    @property
    def serialize(self):
        # Returns object data in easily serializable format
        return{
            'name': self.name,
            'email': self.email,
            'id': self.id,
            'inscription_date': self.inscription_date,
        }


class Machine(Base):
    __tablename__ = 'machine'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    machine_type = Column(String(250), nullable=False)
    company = Column(String(250))
    description = Column(String(250))
    picture = Column(String(250), default="blank_machine.png")
    price = Column(Integer)  # euros

    @property
    def serialize(self):
        # Returns object data in easily serializable format
        return {
            'name': self.name,
            'machine_type': self.machine_type,
            'id': self.id,
            'description': self.description,
            'price': self.price,
            'company': self.company,
        }


class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    description = Column(String(450))
    picture = Column(String(250), default="blank_project.png")
    source = Column(String(850))
    end_date = Column(String(10))  # DD/MM/YY
    member_id = Column(Integer, ForeignKey('member.id'))
    member = relationship(Member)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
            'description': self.description,
            'source': self.source,
            'end_date': self.end_date,
            'member_id': self.member_id,
        }


class Tag(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    tag_name = Column(String(100), nullable=False)
    project_id = Column(Integer, ForeignKey('project.id'))
    project = relationship(Project)


engine = create_engine('sqlite:///lepetitfablabdeparis.db', encoding='utf-8')
Base.metadata.create_all(engine)
