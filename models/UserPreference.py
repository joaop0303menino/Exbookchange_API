from models.Base import Base
from models.Users import User
from models.Authors import Author 

from sqlalchemy import String, ForeignKey, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column, relationship

class UserPreference(Base):
    __tablename__ = 'user_preference'

    id: Mapped[int] = mapped_column(primary_key=True)
    title_book: Mapped[str] = mapped_column(String(255))
    image_book: Mapped[bytes] = mapped_column(LargeBinary)

    #foreign keys
    id_user: Mapped[int] = mapped_column(ForeignKey('users.id'))
    id_author: Mapped[int] = mapped_column(ForeignKey('authors.id'))

    #relations
    user: Mapped['User'] = relationship(back_populates='user_preference')
    authors: Mapped['Author'] = relationship(back_populates='user_preference')