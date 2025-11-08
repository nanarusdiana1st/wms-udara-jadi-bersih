from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import auth, materials, qr, stock_opname, mrp, reports, dashboard
from .database import engine
from .models import Base

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(materials.router)
app.include_router(qr.router)
app.include_router(stock_opname.router)
app.include_router(mrp.router)
app.include_router(reports.router)
app.include_router(dashboard.router)

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to PT. Udara Jadi Bersih WMS!"}
