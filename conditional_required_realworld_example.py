from pydantic import BaseModel, model_validator, ValidationError
from typing import Optional

class AuthPayload(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None
    jwt: Optional[str] = None
    cookie: Optional[str] = None

    @model_validator(mode="after")
    def validate_conditional_required_fields(cls, values):
        c1 = all([values.email, values.password])
        c2 = values.jwt is not None
        c3 = values.cookie is not None

        if sum([c1, c2, c3]) != 1:
            raise ValueError('email/password, jwt, or cookie is required')
        else:
            return values

AuthPayload(
    email='xxx@yyy',
    password='password01234'
)

AuthPayload(
    jwt='some.jwt.token'
)

AuthPayload(
    cookie='some.cookie'
)

try:
    AuthPayload()
except ValidationError as e:
    pass

try:
    AuthPayload(
        email='xxx@yyy',
    )
except ValidationError as e:
    pass

try:
    AuthPayload(
        password='password01234'
    )
except ValidationError as e:
    pass

try:
    AuthPayload(
        email='xxx@yyy',
        password='password01234',
        jwt='some.jwt.token'
    )
except ValidationError as e:
    pass

try:
    AuthPayload(
        email='xxx@yyy',
        password='password01234',
        cookie='some.cookie'
    )
except ValidationError as e:
    pass
