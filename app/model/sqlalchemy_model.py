"""
This file defines the SQLAlchemy model for the database.
"""
import yaml
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Load config from YAML file
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

SQLALCHEMY_DATABASE_URL = config['database']['url']

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Orders(Base):
    """
    id: primary key (unique)
    大訂單號碼: big_order_id
    訂單號碼: small_order_id
    訂單日期: order_date
    顧客: customer
    電話號碼: phone
    電郵: email
    商品貨號: product_id
    商品名稱: product_name
    數量: quantity
    商品類型: product_type (can be null)
    送貨方式: delivery_method
    """
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    big_order_id = Column(String, index=True)
    small_order_id = Column(String)
    order_date = Column(String)
    customer = Column(String, index=True)
    phone = Column(String)
    email = Column(String)
    product_id = Column(String, index=True)
    product_name = Column(String)
    quantity = Column(Integer)
    product_type = Column(String)
    delivery_method = Column(String)
    

Base.metadata.create_all(bind=engine)