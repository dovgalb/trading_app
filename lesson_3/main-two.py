from typing import List

from fastapi import FastAPI
from pydantic.fields import Field
from pydantic.main import BaseModel

app = FastAPI(
    title="Trading App"
)

fake_users = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
    {"id": 4, "role": "investor", "name": "Homer", "degree": [
        {'id': 1, "created_at": "2020-01-01T00:00:00", "type_degree": "expert"}
    ]},
]

fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 124, "amount": 2.12},
    {"id": 3, "user_id": 2, "currency": "BTC", "side": "buy", "price": 121, "amount": 2.2},
]


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=3)
    side: str
    price: float = Field(ge=0)
    amount: float


class User(BaseModel):
    id: int
    role: str
    name: str


@app.post("/trades")
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {"status": "200", "data": fake_trades}


@app.post('/add_user')
def add_user():
    pass



@app.get('/users/{user_id}', response_model=List[User])
def get_user(user_id: int):
    return [user for user in fake_users if user.get('id') == user_id]


@app.get('/users/')
def show_all_users():
    return fake_users
