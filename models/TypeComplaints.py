from models.Base import Base
from models.Complaints import Complaint 

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class TypeComplaint(Base): 
    __tablename__ = 'type_complaints'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[String] = mapped_column(String(255))

    #foreign key
    id_complaint: Mapped[int] = mapped_column(ForeignKey('complaints.id'))

    #relation
    complaint: Mapped['Complaint'] = relationship(back_populates='type_complaints')