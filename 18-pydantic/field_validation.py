from pydantic import BaseModel, field_validator, model_validator


class User(BaseModel):
    username:str

    # @field_validator('username', mode="before") # username type is not validated yet
    # @classmethod
    # def validate_username(cls, username):
    #     print(cls)
    #     if len(username) < 4:
    #         raise ValueError("Username must be atleast 4 characters")
    #     return username.strip()

    @field_validator('username', mode="before") # username type is validated and confirmed it is string
    @classmethod
    def validate_username(cls, username:str) -> str:
        print(cls)
        if len(username) < 4:
            raise ValueError("Username must be atleast 4 characters")
        return username.strip()

    


class SignUpData(BaseModel):
    password:str
    confirm_password: str

    # @model_validator(mode="after")
    # def is_password_match(self):
    #     print(type(self))
    #     if self.password != self.confirm_password:
    #         raise ValueError("Password and confirm password did not match")
    #     return self


    @model_validator(mode="before")
    @classmethod
    def is_password_match(cls, values):
        print(type(values))
        password = values['password']
        confirm_password = values['confirm_password']
        if password != confirm_password:
            raise ValueError("Password and confirm password did not match")
        return values


user = User(username="ddddd")  
