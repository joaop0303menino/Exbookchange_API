from models.Base import Base
from models.Users import User
from models.ConservationStatus import ConservationStatus
from models.Authors import Author
from models.ExchangeDonation import ExchangeDonation
from models.ImagesBook import ImagesBook

from enum import Enum
from sqlalchemy import Enum as SQLAlchemyEnum

from typing import List
from sqlalchemy import String, TIMESTAMP, Boolean, ForeignKey, Text
from datetime import date, datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship

class IsExchangeDonationEnum(Enum):
    exchange = "Exchange"
    donation = "Donation"



class Announce(Base):
    __tablename__ = "announces"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)
    is_exchange_donation: Mapped[IsExchangeDonationEnum] = mapped_column(
        SQLAlchemyEnum(IsExchangeDonationEnum, name = "exchange_donation_enum", native_enum=False)
    )
    archived: Mapped[bool] = mapped_column(Boolean, default = False)
    posted_at: Mapped[datetime] = mapped_column(TIMESTAMP, nullable = True)

    #foreign key's
    id_conservation_status: Mapped[int] = mapped_column(ForeignKey('conservation_status.id'))
    id_user: Mapped[int] = mapped_column(ForeignKey("user.id"))
    id_author: Mapped[int] = mapped_column(ForeignKey('authors.id'))

    #relations
    conservation_status: Mapped['ConservationStatus'] = relationship(back_populates = 'announces')
    user: Mapped["User"] = relationship(back_populates = 'announces')
    author: Mapped['Author'] = relationship(back_populates = 'announce')
    exchange_donation: Mapped['ExchangeDonation'] = relationship(back_populates='announces')
    images_book: Mapped[List['ImagesBook']] = relationship(back_populates='announce')  
