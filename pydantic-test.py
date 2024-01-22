from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: int
    name: str
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

external_data = {
    'id': '123',
    'name': 'John Doe',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3']
}

user = User(**external_data)

assert user.id == 123
assert user.signup_ts == datetime(2019, 6, 1, 12, 22)
assert user.friends == [1, 2, 3]

# Optional fields are allowed to be None
external_data2 = {
    'id': 1,
    'name': 'John Doe',
    'signup_ts': '2019-06-01 12:22'
}
user2 = User(**external_data2)
assert user2.friends == []
