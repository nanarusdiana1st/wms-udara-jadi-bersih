from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base
from .user import User

class StockOpname(Base):
    __tablename__ = "stock_opname"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(50))
    date = Column(Date, nullable=False)
    total_materials = Column(Integer)
    accuracy_percentage = Column(Float)
    created_by_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.utcnow)

    created_by = relationship("User", back_populates="stock_opname")