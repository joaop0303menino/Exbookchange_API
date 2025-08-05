from models.Base import Base
from models.Announces import Announce

from enum import Enum
from sqlalchemy import Enum as SQLAlchemyEnum

from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column, relationship


class ConservationStatusEnum(Enum):
    UM = 1
    DOIS = 2
    TRES = 3
    QUATRO = 4
    CINCO = 5


class ConservationStatus(Base):
    __tablename__ = "conservation_status"
    id: Mapped[int] = mapped_column(primary_key=True)
    conservation_status: Mapped[ConservationStatusEnum] = mapped_column(
        SQLAlchemyEnum(ConservationStatusEnum, name="conservation_status_enum", native_enum=False)
    )
    description_status: Mapped[str] = mapped_column(Text)


    #relations
    announces: Mapped['Announce'] = relationship(back_populates = 'conservation_status', uselist=False)
