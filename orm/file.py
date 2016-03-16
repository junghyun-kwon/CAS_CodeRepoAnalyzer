"""
file: commit.py
author: Ben Grawi <bjg1568@rit.edu>, Christoffer Rosen <cbr4830@rit.edu>
date: Novemeber 2013
description: Holds the commit abstraction class and ORM
"""
from db import *
#from sqlalchemy import *

class File(Base):
    """
    Commit():
    description: The SQLAlchemy ORM for the commits table
    """
    __tablename__ = 'files'

    # Many-to-One Relation to repositories table
    repository_id = Column(String)
    commit_hash = Column(String)

    file_name = Column(String)

    __table_args__ = (
        PrimaryKeyConstraint('repository_id', 'commit_hash', 'file_name'),
        {},
    )

    def __init__(self, file):
        """
        __init__(): Dictonary -> NoneType
        """
        self.__dict__.update(file)

    # def __repr__(self):
    #     return "<Commit('%s','%s', '%s', '%s')>" % \
    #         (self.commit_hash,
    #         self.author_name,
    #         self.author_date,
    #         self.commit_message)
