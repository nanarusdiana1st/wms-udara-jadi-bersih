from pydantic import BaseModel
from typing import Optional

class MaterialCreate(BaseModel):
    name: str
    code: str
    category: Optional[str] = None
    unit: Optional[str] = None
    description: Optional[str] = None
    stock_quantity: float = 0.0
    min_stock_level: float = 0.0
    max_stock_level: float = 0.0
    price_per_unit: float = 0.0
    status: str = "active"
    expiry_date: Optional[str] = None

class MaterialUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    category: Optional[str] = None
    unit: Optional[str] = None
    description: Optional[str] = None
    stock_quantity: Optional[float] = None
    min_stock_level: Optional[float] = None
    max_stock_level: Optional[float] = None
    price_per_unit: Optional[float] = None
    status: Optional[str] = None
    expiry_date: Optional[str] = None

class MaterialResponse(BaseModel):
    id: int
    name: str
    code: str
    category: Optional[str] = None
    unit: Optional[str] = None
    description: Optional[str] = None
    stock_quantity: float
    min_stock_level: float
    max_stock_level: float
    price_per_unit: float
    status: str
    expiry_date: Optional[str] = None
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True