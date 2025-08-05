from models.Base import Base
from models.Notifications import Notification

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class TypeNotification(Base):
    __tablename__ = 'type_notification'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))

    #relation
    notification: Mapped['Notification'] = relationship(back_populates = 'type_notification')