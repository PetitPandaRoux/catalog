from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from setup_database import Base, Member, Machine, Project, Tag

engine = create_engine('sqlite:///lepetitfablabdeparis.db', encoding='utf-8')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()

member1 = Member(name="Laurent", email="barnier.lrnt@gmail.com", inscription_date="10/02/18" )
session.add(member1)
session.commit()

member2 = Member(name="Sakada", email="lysakada@gmail.com", inscription_date="10/10/17")
session.add(member2)
session.commit()

member3 = Member(name="Izar", email="izarmediavilla@gmail.com", inscription_date="10/09/16")
session.add(member3)
session.commit()

member4 = Member(name="Adel", email="adel@gmail.com", inscription_date="01/10/17")
session.add(member4)
session.commit()

machine1 = Machine(name = "60W CO2 laser cutter", machine_type = "Laser cutter", quantity = 1, company = "Unknow", price = 5000, description = "Laser Cut of 60W from China. It can cut to 8mm plywood")
session.add(machine1)
session.commit()

machine2 = Machine(name = "Zortrax M500", machine_type = "3D printer", quantity = 1, company = "Zortrax", price = 2000, description = "Proprietary 3D printing machine using ABS")
session.add(machine2)
session.commit()

machine3 = Machine(name="Ultimaker2", machine_type="3D printer", quantity=1, company="Ultimaker", price=2000, description="")
session.add(machine3)
session.commit()

project1 = Project(name='Sky_Paper_Light_Box',source="https://www.instructables.com/id/Paper-Cut-Light-Box-for-Sky/",description="An artistic representation using light and paper", end_date="01/01/18", member=member2)
session.add(project1)
session.commit()

project2 = Project(name="Countdown Events Box", description="A box and a set of NFC card that remind you the number of day before an event",source="https://www.instructables.com/id/Countdown-Events-Box/", end_date="01/05/17", member=member1 )
session.add(project2)
session.commit()


tag1 = Tag(project=project1, tag_name="Arduino")
session.add(tag1)
session.commit()

tag2 = Tag(project=project1, tag_name="Vinyl cut")
session.add(tag2)
session.commit()

tag3 = Tag(project=project1, tag_name="Laser Cut")
session.add(tag3)
session.commit()

tag4 = Tag(project=project2, tag_name="Arduino")
session.add(tag4)
session.commit()

tag5 = Tag(project=project2, tag_name="3D printing")
session.add(tag4)
session.commit()

print "added menu items!"
session.close()