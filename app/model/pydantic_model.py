"""
This file contains the pydantic models for the API.
"""
from pydantic import BaseModel, Field

class Orders(BaseModel):
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
    id: int = Field(..., example="1")
    big_order_id: str = Field(..., example="B000")
    small_order_id: str = Field(..., example="#20230703021032226")
    order_date: str = Field(..., example="07/03/2023 10:10:32")
    customer: str = Field(..., example="歐于綸")
    phone: str = Field(..., example="0930075728")
    email: str = Field(..., example="tingyu.wang12@gmail.com")
    product_id: str = Field(..., example="A10103001")
    product_name: str = Field(..., example="Pattis 青潤保濕精萃蜜 30mL")
    quantity: int = Field(..., example="1")
    product_type: str = Field(..., example="")
    delivery_method: str = Field(..., example="11")