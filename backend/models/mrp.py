from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from datetime import datetime
from .database import Base
from .material import Material

class MRP(Base):
    __tablename__ = "mrp_calculations"

    id = Column(Integer, primary_key=True, index=True)
    material_id = Column(Integer, ForeignKey('materials.id'))
    period = Column(String(10))  # 3_months, 6_months, 12_months
    avg_usage = Column(Float)
    safety_stock = Column(Float)
    reorder_point = Column(Float)
    suggested_order_qty = Column(Float)
    calculated_at = Column(DateTime, default=datetime.utcnow)

    material = relationship("Material", back_populates="mrp_calculations")