from datetime import datetime, timedelta
from typing import List, Dict
from sqlalchemy.orm import Session
from ..models import Material, StockHistory

def calculate_dead_stock(db: Session) -> Dict:
    dead_stock_threshold_days = 365
    now = datetime.now()
    dead_stock = []
    total_value = 0

    for material in db.query(Material).all():
        last_used = db.query(StockHistory).filter(StockHistory.material_id == material.id).order_by(StockHistory.created_at.desc()).first()
        if last_used and (now - last_used.created_at).days > dead_stock_threshold_days:
            dead_stock.append({
                'name': material.name,
                'quantity': material.stock_quantity,
                'value': material.stock_quantity * material.price_per_unit
            })
            total_value += material.stock_quantity * material.price_per_unit

    return {
        'items': dead_stock,
        'total_quantity': sum(item['quantity'] for item in dead_stock),
        'total_value': total_value
    }

def calculate_slow_moving(db: Session) -> Dict:
    slow_moving_threshold_days = 90
    now = datetime.now()
    slow_moving = []
    total_value = 0

    for material in db.query(Material).all():
        last_used = db.query(StockHistory).filter(StockHistory.material_id == material.id).order_by(StockHistory.created_at.desc()).first()
        if last_used and (now - last_used.created_at).days > slow_moving_threshold_days:
            slow_moving.append({
                'name': material.name,
                'quantity': material.stock_quantity,
                'value': material.stock_quantity * material.price_per_unit
            })
            total_value += material.stock_quantity * material.price_per_unit

    return {
        'items': slow_moving,
        'total_quantity': sum(item['quantity'] for item in slow_moving),
        'total_value': total_value
    }

def calculate_avg_usage(db: Session, material_id: int, period: str = '3_months') -> float:
    months = {'3_months': 3, '6_months': 6, '12_months': 12}
    start_date = datetime.now() - timedelta(days=months[period] * 30)
    usage = db.query(StockHistory).filter(
        StockHistory.material_id == material_id,
        StockHistory.type == 'out',
        StockHistory.created_at >= start_date
    ).all()
    return sum(u.quantity_change for u in usage) / len(usage) if usage else 0

def calculate_mrp(db: Session, material_id: int) -> Dict:
    material = db.query(Material).filter(Material.id == material_id).first()
    avg_3m = calculate_avg_usage(db, material_id, '3_months')
    avg_6m = calculate_avg_usage(db, material_id, '6_months')
    avg_12m = calculate_avg_usage(db, material_id, '12_months')

    safety_stock = avg_3m * 0.5
    reorder_point = safety_stock + avg_3m
    suggested_order = reorder_point - material.stock_quantity

    return {
        'avg_3m': avg_3m,
        'avg_6m': avg_6m,
        'avg_12m': avg_12m,
        'safety_stock': safety_stock,
        'reorder_point': reorder_point,
        'suggested_order': suggested_order
    }