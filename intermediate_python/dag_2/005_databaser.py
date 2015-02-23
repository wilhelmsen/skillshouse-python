#!/usr/bin/python
# coding: utf-8




#
# installer pyodbc i dit virtualenv
#
# vitualenv dag2
# . dag2/bin/activate
# pip install SQLAlchemy
#
# SQLAlchemy er en ORM eller en Object relational manager. Det betyder at den
# kan afbilde python objekter til rækker og relationer i databasen. ORM'en gør
# det næsten usynligt at objektet findes i databasen.

# opret databasen
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)

# Der er flere måder at kører ORM'en på. Enten på en eksisterende database
# ellers på en blank database. Det sidste er det nemmeste. Med declarative base
# bliver tabellerne automatisk oprettet i databasen hvis ikke de eksisterer.
# Det er den bedste måde at bruge SQLAlchemy.

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


# nu skal vi definerer et objekt.

from sqlalchemy import Column, Integer, String
class User(Base):

    # vi angiver et tabelnavn
    __tablename__ = 'users'

    # vi definere nogle kolonner
    id = Column(Integer, primary_key=True)

    # navnet må ikke være blankt, database constraint
    name = Column(String, nullable=False)
    fullname = Column(String)
    password = Column(String)

    # default repræsentation af objektet
    def __repr__(self):
       return "<User(name='%s', fullname='%s', password='%s')>" % (
                            self.name, self.fullname, self.password)

# opret alle de tabeller der ikke allerede findes
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
# Opret en Session klasse dynamis
Session = sessionmaker(bind=engine)

# start en session fra klassen
session = Session()

# lav en bruger 
bruger = User(name="Lars", fullname="Lars Ulrik", password="Heavy")

# opret brugeren i databasen

session.add(bruger)

# Spørg efter brugeren

brugere = session.query(User).filter_by(name="Lars").all()

for b in brugere:
    print b

# update user
b.password = "Metal"
# og gem med comit
session.commit()

# vi vil kun have en
lars = session.query(User).filter_by(name="Lars").one()
print lars.password

# vi giver ikke lars lige nu
session.delete(lars)
session.commit()

# ingen lars'er tilbage
print session.query(User).filter_by(name="Lars").count()









