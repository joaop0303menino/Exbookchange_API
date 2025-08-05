from models.Base import Base
from models.Users import User

from sqlalchemy import ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship


class UserSetting(Base):
    __tablename__ = 'user_settings'

    id: Mapped[int] = mapped_column(primary_key = True)
    receiveNotifications: Mapped[bool] = mapped_column(Boolean)

    #foreign keys
    id_user: Mapped[int] = mapped_column(ForeignKey('users.id'))

    #relations
    user: Mapped["User"] = relationship(back_populates='user_settings')