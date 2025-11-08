from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Material, User
from ..schemas import MaterialCreate, MaterialUpdate
from ..auth import get_current_user, get_current_admin

router = APIRouter(prefix="/materials", tags=["Materials"])

@router.get("/")
def read_materials(skip: int = 0, limit: int = 100, current_user=Depends(get_current_user), db: Session = Depends(SessionLocal)):
    materials = db.query(Material).offset(skip).limit(limit).all()
    return materials

@router.post("/")
def create_material(material: MaterialCreate, current_user=Depends(get_current_user), db: Session = Depends(SessionLocal)):
    db_material = Material(**material.dict(), created_by_id=current_user.id)
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material

@router.put("/{material_id}")
def update_material(material_id: int, material_update: MaterialUpdate, current_user=Depends(get_current_user), db: Session = Depends(SessionLocal)):
    db_material = db.query(Material).filter(Material.id == material_id).first()
    if not db_material:
        raise HTTPException(status_code=404, detail="Material not found")
    for key, value in material_update.dict(exclude_unset=True).items():
        setattr(db_material, key, value)
    db.commit()
    db.refresh(db_material)
    return db_material

@router.delete("/{material_id}")
def delete_material(material_id: int, current_user=Depends(get_current_admin), db: Session = Depends(SessionLocal)):
    db_material = db.query(Material).filter(Material.id == material_id).first()
    if not db_material:
        raise HTTPException(status_code=404, detail="Material not found")
    db.delete(db_material)
    db.commit()
    return {"message": "Material deleted successfully"}