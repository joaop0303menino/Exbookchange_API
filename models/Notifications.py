from models.Base import Base
from models.Profiles import Profile
from models.Users import User
from models.TypeNotification import TypeNotification

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Notification(Base):
    __tablename__ = 'notifications'

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(Text)

    #foreign keys
    id_profile: Mapped[int] = mapped_column(ForeignKey('profiles.id'))
    id_user: Mapped[int] = mapped_column(ForeignKey('users.id'))
    id_type_notification: Mapped[int] = mapped_column(ForeignKey('type_notification.id'))

    #relations
    profile: Mapped['Profile'] = relationship(back_populates='notifications')
    user: Mapped['User'] = relationship(back_populates='notifications')
    type_notification: Mapped['TypeNotification'] = relationship(back_populates='notification')