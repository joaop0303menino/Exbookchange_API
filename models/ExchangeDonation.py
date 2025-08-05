from models.Base import Base
from models.Users import User
from models.Announces import Announce
from models.ExchangeDonationHistoric import ExchangeDonationHistoric

from typing import List
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class ExchangeDonation(Base):
    __tablename__ = 'exchange_donations'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_receiver: Mapped[str] = mapped_column(String(100))

    #foreign keys
    id_user: Mapped[int] = mapped_column(ForeignKey('users.id'))
    id_announces: Mapped[int] = mapped_column(ForeignKey('announces.id'))
    
    #relations 
    user: Mapped['User'] = relationship(back_populates= 'exchange_donations')
    announces: Mapped['Announce'] = relationship(back_populates='exchange_donations', uselist=False)
    exchange_donation_historic: Mapped['ExchangeDonationHistoric'] = relationship(back_populates='exchange_donation')