from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base
from .material import Material

class StockHistory(Base):
    __tablename__ = "stock_history"

    id = Column(Integer, primary_key=True, index=True)
    material_id = Column(Integer, ForeignKey('materials.id'))
    quantity_change = Column(Float)
    type = Column(String(20))  # in, out, opname
    note = Column(String(500))
    created_at = Column(DateTime, default=datetime.utcnow)

    material = relationship("Material", back_populates="stock_history")