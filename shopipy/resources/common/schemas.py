from typing import Optional
from pydantic import BaseModel


class ShopMoney(BaseModel):
    amount: Optional[str]
    currency_code: Optional[str]


class AmountSet(BaseModel):
    shop_money: Optional[ShopMoney]
    presentment_money: Optional[ShopMoney]


class TaxItem(BaseModel):
    title: Optional[str]
    price: Optional[str]
    price_set: Optional[AmountSet]
    rate: Optional[str]
    channel_liable: Optional[str]