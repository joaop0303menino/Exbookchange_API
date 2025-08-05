from models.Base import Base
from models.Announces import Announce

from sqlalchemy import LargeBinary, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class ImagesBook(Base):
    __tablename__ = 'images_book'

    id: Mapped[int] = mapped_column(primary_key=True)
    image: Mapped[bytes] = mapped_column(LargeBinary)
    is_cover: Mapped[bool] = mapped_column(Boolean, default=False)

    #foreign keys
    id_announce: Mapped[int] = mapped_column(ForeignKey('announces.id'))

    #relations
    announce: Mapped['Announce'] = relationship(back_populates='images_book')