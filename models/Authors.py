from models.Base import Base
from models.Announces import Announce
from models.UserPreference import UserPreference

from typing import List
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Author(Base):
    __tablename__ = "authors"
    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str]= mapped_column(String)


    #relation
    announce: Mapped['Announce'] = relationship(back_populates = 'author', uselist=False)
    user_preference: Mapped[List['UserPreference']] = relationship(back_populates = 'authors')
