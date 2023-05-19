from pydantic import BaseModel


class Grocery(BaseModel):
    item_id: int
    name: str
    quantity: int
    amount: float


class Email(BaseModel):
    rec_email: str
    subject: str
    body: str
