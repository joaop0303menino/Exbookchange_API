from models.Base import Base
from models.UserSettings import UserSetting
from models.Announces import Announces
from models.ExchangeDonation import ExchangeDonation
from models.UserPreference import UserPreference
from models.Profiles import Profile
from models.Notifications import Notification
from models.Complaints import Complaint

from typing import Optional, List
from sqlalchemy import String, TIMESTAMP
from datetime import date, datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship




class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(100))
    date_birth: Mapped[Optional[date]] = mapped_column(nullable=True)  
    email: Mapped[str] = mapped_column(String(120), unique=True)
    password: Mapped[str] = mapped_column(String(255))
    phone: Mapped[Optional[str]] = mapped_column(String(11), nullable=True)
    created_at: Mapped[Optional[datetime]] = mapped_column(TIMESTAMP, nullable=True)  
    updated_at: Mapped[Optional[datetime]] = mapped_column(TIMESTAMP, nullable=True)  
    trust_seal: Mapped[bool] = mapped_column(default=False)
    blocked_user: Mapped[bool] = mapped_column(default=False)

    #relations
    user_settings: Mapped["UserSetting"] = relationship(back_populates = "user", uselist=False) #relação 1 para 1 com tabela UserSettigs
    announces: Mapped[List["Announces"]] = relationship(back_populates = 'user')
    exchange_donations: Mapped[List['ExchangeDonation']] = relationship(back_populates = 'user')
    user_preference: Mapped[List['UserPreference']] = relationship(back_populates = 'user')
    profile: Mapped['Profile'] = relationship(back_populates='user')
    notifications: Mapped[List['Notification']] = relationship(back_populates='notification')
    complaints: Mapped[List['Complaint']] = relationship(back_populates='user')