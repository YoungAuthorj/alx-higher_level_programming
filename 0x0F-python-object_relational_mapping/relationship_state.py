Skip to content
Search or jump to…
Pulls
Issues
Codespaces
Marketplace
Explore
 
@YoungAuthorj 
proyirga
/
alx-higher_level_programming
Public
Fork your own copy of proyirga/alx-higher_level_programming
Code
Issues
Pull requests
Actions
Projects
Security
Insights
alx-higher_level_programming/0x0F-python-object_relational_mapping/relationship_state.py /
@yirgamulaw
yirgamulaw 0x0F-python-object_relational_mapping
Latest commit f0602b7 2 weeks ago
 History
 1 contributor
Executable File  26 lines (21 sloc)  745 Bytes

#!/usr/bin/python3
"""
This script defines a State class and
a Base class to work with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class
    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class
        cities (:obj:`City`): The Cities belongs to State
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
