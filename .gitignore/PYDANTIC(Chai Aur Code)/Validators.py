from pydantic import field_validator, model_validator, computed_field , BaseModel

class user(BaseModel):
    username:str

    @field_validator('username')
    def username_length(cls,v):
        if len(v)<4:
            raise ValueError("user name must be at least 4 character")
        return v

class signup_data(BaseModel):
    password:str
    confirm_password:str

    @model_validator(mode='after')
    def password_match(cls,values):
        if values.password!=values.confirm_password:
            raise ValueError('password do not match')
        return values
    


class product(BaseModel):
    price:float
    quantity:int

    @computed_field
    @property
    def total_price(self)->float:
        return self.float*self.quantity
