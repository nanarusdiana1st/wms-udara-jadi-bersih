from sqlalchemy import Column, Integer, String, Float, Date, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base
from .user import User

class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    code = Column(String(50), unique=True, nullable=False)
    category = Column(String(50))
    unit = Column(String(20))
    description = Column(String(500))
    stock_quantity = Column(Float, default=0.0)
    min_stock_level = Column(Float, default=0.0)
    max_stock_level = Column(Float, default=0.0)
    price_per_unit = Column(Float, default=0.0)
    status = Column(String(20), default="active")  # active, inactive_temp, inactive_perm
    expiry_date = Column(Date)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    created_by_id = Column(Integer, ForeignKey('users.id'))
    created_by = relationship("User", back_populates="materials")

    stock_history = relationship("StockHistory", back_populates="material")
    notifications = relationship("Notification", back_populates="material")