from models.Base import Base
from models.Users import User
from models.Notifications import Notification
from models.Reviews import Review
from models.Complaints import Complaint

from typing import List
from sqlalchemy import String, LargeBinary, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Profile(Base): 
    __tablename__ = 'profiles'

    id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(Text)
    photo: Mapped[bytes] = mapped_column(LargeBinary)

    #foreign keys
    id_user: Mapped[int] = mapped_column(ForeignKey('users.id'))

    #relations 
    user: Mapped['User'] = relationship(back_populates='profile', uselist=False)
    notifications: Mapped[List['Notification']] = relationship(back_populates='profile')
    reviews: Mapped[List['Review']] = relationship(back_populates='profile')
    complaints: Mapped[List['Complaint']] = relationship(back_populates='profile')