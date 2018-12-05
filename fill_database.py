from setup_database import Base, Machine, Member, Project, Tag
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lepetitfablabdeparis.db', encoding='utf-8')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()

member1 = Member(name="Laurent", email="barnier.lrnt@gmail.com", inscription_date="10/02/18", picture="laurent.png" )
session.add(member1)
session.commit()

member2 = Member(name="Sakada", email="lysakada@gmail.com", inscription_date="10/10/17", picture="sakada.png")
session.add(member2)
session.commit()

member3 = Member(name="Izar", email="izarmediavilla@gmail.com", inscription_date="10/09/16", picture="izar.png")
session.add(member3)
session.commit()

member4 = Member(name="Adel", email="adel@gmail.com", inscription_date="01/10/17", picture="adel.png")
session.add(member4)
session.commit()

machine1 = Machine(name = "60W CO2 laser cutter", machine_type = "Laser cutter", quantity = 1, company = "Unknow", price = 5000, description = "Laser Cut of 60W from China. It can cut to 8mm plywood", picture = "laser.jpg")
session.add(machine1)
session.commit()

machine2 = Machine(name = "Zortrax M500", machine_type = "3D printer", quantity = 1, company = "Zortrax", price = 2000, description = "Proprietary 3D printing machine using ABS", picture = "zortrax.jpg")
session.add(machine2)
session.commit()

machine3 = Machine(name="Ultimaker2", machine_type="3D printer", quantity=1, company="Ultimaker", price=2000, description="", picture = "ultimaker.jpg")
session.add(machine3)
session.commit()

project1 = Project(name='Sky_Paper_Light_Box',source="https://www.instructables.com/id/Paper-Cut-Light-Box-for-Sky/",description="An artistic representation using light and paper. The art style of the series is so unique, full of clean colors and warm lights, which matches Hari & Deepti's paper cut light box perfectly. Inspired by their masterpieces, I decide to DIY a light box for thatgamecompany's newest title 'Sky' in this project", end_date="01/01/18", member=member2)
session.add(project1)
session.commit()

tag1 = Tag(project=project1, tag_name="Arduino")
session.add(tag1)
session.commit()

tag2 = Tag(project=project1, tag_name="Laser Cutter")
session.add(tag2)
session.commit()

project2 = Project(name="Floor Table", description="Quick and lightweight, this recycled table is at home on hardwood or concrete.  As long as the wood is salvaged, the materials will cost only a few dollars -- a little finish, a few dollops of glue, and a handful of screws.  ",source="https://www.instructables.com/id/Floor-Table/", end_date="01/05/17", member=member1 )
session.add(project2)
session.commit()

tag3 = Tag(project=project2, tag_name="Portable Electric")
session.add(tag3)
session.commit()

project3 = Project(name="Butt Table", description="A Butt Table is a table made from the butt slices of a tree.  Here is one way to make yourself a butt table.",source="https://www.instructables.com/id/Butt-Table/", end_date="10/02/17", member=member1 )
session.add(project3)
session.commit()

tag4 = Tag(project=project3, tag_name="Portable Electric")
session.add(tag4)
session.commit()

project4 = Project(name="Interactive Arduino Powered Coffee Table", description="The design of the table aspect was inspired mainly from another table I had seen with a similar arched shape but with a flat top, and the electronics were mainly inspire from this coffee table, although I wanted something easier so I used a 16x16 single colour matrix and two LCD displays on my table, there is also an audio amplifier and Bluetooth receiver for playing music through the table.",source="https://www.instructables.com/id/Interactive-Arduino-Powered-Coffee-Table/", end_date="14/05/17", member=member3 )
session.add(project4)
session.commit()

tag5 = Tag(project=project4, tag_name="Portable Electric")
session.add(tag5)
session.commit()

tag6 = Tag(project=project4, tag_name="Arduino")
session.add(tag6)
session.commit()

project5 = Project(name="Countdown Events Box", description="Countdown Events Box is an incredible IOT vintage machine. It displays the number of remote days of important life events. Each event is symbolized by a NFC card with a custom text, picture or drawing. If you put one of them on the Countdown Events Box front panel, then the number of remote days is displayed.",source="https://www.instructables.com/id/Countdown-Events-Box/", end_date="05/05/16", member=member3 )
session.add(project5)
session.commit()

tag7 = Tag(project=project5, tag_name="Laser Cutter")
session.add(tag7)
session.commit()

tag8 = Tag(project=project5, tag_name="Arduino")
session.add(tag8)
session.commit()

tag9 = Tag(project=project5, tag_name="3D Printer")
session.add(tag9)
session.commit()

project6 = Project(name="Plank Chair", description="A simple and satisfying chair made from one plank of wood. ",source="https://www.instructables.com/id/Plank-Chair/", end_date="04/06/15", member=member4 )
session.add(project6)
session.commit()

tag10 = Tag(project=project6, tag_name="Portable Electric")
session.add(tag10)
session.commit()

tag11 = Tag(project=project6, tag_name="Laser Cutter")
session.add(tag11)
session.commit()

project7 = Project(name="DIY Weather Station & WiFi Sensor Station", description="The sensor station measures local temperature and humidity data and sends it, through WiFi, to the weather station. The weather station then displays the data on its LCD screen. It also grabs the current temperature and humidity data in your city from the Internet and displays it as well on the LCD screen",source="https://www.instructables.com/id/DIY-Weather-Station-WiFi-Sensor-Station/", end_date="10/02/17", member=member2 )
session.add(project7)
session.commit()

tag12 = Tag(project=project7, tag_name="Arduino")
session.add(tag12)
session.commit()

tag13 = Tag(project=project7, tag_name="3D Printer")
session.add(tag13)
session.commit()

project8 = Project(name="Avatar PlaNT (Touch Sensitive)", description="It is an avatar plant with LEDs all around. Once the plant is touched, LED turns on. You only need to use several LEDs and resistors with arduino. Of course, if you want to light up an avatar  forest, you can also connect all plants together",source="https://www.instructables.com/id/Avatar-PlaNT-Touch-Sensitive/", end_date="21/08/17", member=member3 )
session.add(project8)
session.commit()

tag14 = Tag(project=project8, tag_name="Arduino")
session.add(tag14)
session.commit()

project9 = Project(name="3D Print a Chess Set", description="In just eight steps you will have a complete chess set ready to be printed.  I chose the chess set for this instructable because unlike many possessions a person owns, a chess set needs to be shared to be enjoyed",source="https://www.instructables.com/id/3D-Print-A-Chess-Set/", end_date="01/05/17", member=member2 )
session.add(project9)
session.commit()

tag15 = Tag(project=project9, tag_name="3D Printer")
session.add(tag15)
session.commit()

project10 = Project(name="Light Fixture", description="I recently moved to a new desk at work and I wanted to liven up the space a bit, so I made this light fixture. This was a very quick project to make, and it turned out looking pretty good!",source="https://www.instructables.com/id/Laser-Cut-Light-Fixture/", end_date="17/03/18", member=member3 )
session.add(project10)
session.commit()

tag16 = Tag(project=project10, tag_name="Arduino")
session.add(tag16)
session.commit()

tag17 = Tag(project=project10, tag_name="Laser Cutter")
session.add(tag17)
session.commit()

project11 = Project(name="Laser Cut Analog Clock", description="Inspired by the giant clock in the Crocker Galleria in San Francisco, I set out to create an 18' version for hanging at home.  I loved the look of the Roman numerals, and the idea of combining an analog clock with the technology of lasers!  I cut the all pieces on an Epilog laser cutter, but you can use the free files I included for you to make your own using whatever method you prefer",source="https://www.instructables.com/id/Laser-Cut-Analog-Clock/", end_date="25/09/16", member=member1 )
session.add(project11)
session.commit()

tag18 = Tag(project=project11, tag_name="Laser Cutter")
session.add(tag18)
session.commit()

project12 = Project(name="3d Printed Puzzle", description="A puzzle game composed by a dozen of 3D tiles can be printed to reach a remarkable size, and it will be a very appreciated present. If Easter is coming you can also decide to make an egg shape instead of the classical cube",source="https://www.instructables.com/id/3d-printed-puzzle/", end_date="01/12/17", member=member2 )
session.add(project12)
session.commit()

tag19 = Tag(project=project12, tag_name="Arduino")
session.add(tag19)
session.commit()

print "added menu items!"
session.close()
