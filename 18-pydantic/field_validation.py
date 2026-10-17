from pydantic import BaseModel, field_validator, model_validator


class User(BaseModel):
    username:str

    @field_validator('username')
    def validate_username(cls,value):
        if len(value) < 4:
            raise ValueError("Username must be atleast 4 characters")
        return value.strip()


class SignUpData(BaseModel):
    password:str
    confirm_password: str

    @model_validator(mode="after")
    def is_password_match(cls, values):
        print(cls)
        if values.password != values.confirm_password:
            raise ValueError("Password and confirm password did not match")
        return values


signup_data = SignUpData(password="ABCSS", confirm_password="ABCSSD")
print(signup_data)    
