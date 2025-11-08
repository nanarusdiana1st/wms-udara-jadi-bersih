from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from datetime import datetime
from .database import Base
from .user import User
from .material import Material

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    material_id = Column(Integer, ForeignKey('materials.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    type = Column(String(20))  # low_stock, expired, mrp_alert
    message = Column(String(500))
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    material = relationship("Material", back_populates="notifications")
    user = relationship("User", back_populates="notifications")