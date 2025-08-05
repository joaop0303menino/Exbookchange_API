from models.Base import Base
from models.ExchangeDonation import ExchangeDonation

from datetime import date
from sqlalchemy import ForeignKey, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, relationship

class ExchangeDonationHistoric(Base):
    __tablename__ = 'exchange_donation_historic'

    id: Mapped[int] = mapped_column(primary_key=True)
    date_transation: Mapped[date] = mapped_column(TIMESTAMP, nullable=True)

    #foreign key
    id_exchange_donation: Mapped[int] = mapped_column(ForeignKey('exchange_donations.id'))

    #relation
    exchange_donation: Mapped['ExchangeDonation'] = relationship(back_populates='exchange_donation_historic', uselist=False)