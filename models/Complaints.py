from models.Base import Base
from models.Profiles import Profile
from models.Users import User
from models.TypeComplaints import TypeComplaint

from sqlalchemy import ForeignKey, Text, TIMESTAMP 
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Complaint(Base):
    __tablename__ = 'complaints'

    id:  Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(Text)
    
    #foreign keys
    id_profile: Mapped[int] = mapped_column(ForeignKey('profile.id'))
    id_user: Mapped[int] = mapped_column(ForeignKey('user.id'))

    #relations
    profile: Mapped['Profile'] = relationship(back_populates='complaints')
    user: Mapped['User'] = relationship(back_populates='complaints')
    type_complaints: Mapped['TypeComplaint'] = relationship(back_populates='complaint')
