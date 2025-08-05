from models.Base import Base
from models.Profiles import Profile

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Review(Base):
    __tablename__ = 'reviews'

    id: Mapped[int] = mapped_column(primary_key=True)
    ratting: Mapped[int] = mapped_column(Integer, nullable=False, default = 0)

    #foreign key
    id_profile: Mapped[int] = mapped_column(ForeignKey('profiles.id'))

    #relation
    profile: Mapped['Profile'] = relationship(back_populates='reviews')