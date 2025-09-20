from fastapi import FastAPI
from models import product_schema
from database import engine, session
from database_models import products_table
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for all origins (adjust as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def hello():
    return 'hi srk'

@app.get("/products")
def get_products():
    db = session(bind=engine)
    db_products = db.query(products_table).all()
    db.close()
    return db_products

@app.get("/products/{id}")
def get_products(id: int):
    db = session(bind=engine)
    db_products = db.query(products_table).filter(products_table.id == id).first()
    db.close()
    if db_products:
        return db_products
    return "Product Not Found"

@app.post("/products")
def add_product(product_data: product_schema):
    db = session(bind=engine)
    db.add(products_table(name=product_data.name, price=product_data.price, id=product_data.id))
    db.commit()
    db.close()
    return product_data

@app.put('/products')
def update_product(id: int,product_data: product_schema):
    db = session(bind=engine)
    db_products = db.query(products_table).filter(products_table.id == id).first()
    if db_products:
        db_products.name = product_data.name
        db_products.price = product_data.price
        db.commit()
        db.close()
        return product_data
    return "product Not found"
    
@app.delete('/products')
def delete_product(id: int):
    db = session(bind=engine)
    db_products = db.query(products_table).filter(products_table.id == id).first()
    if db_products:
        db.delete(db_products)
        db.commit()
        db.close()
        return "product deleted"
    return "product Not found"