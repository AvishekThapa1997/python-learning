from pydantic import BaseModel
from typing import Optional


class Comment(BaseModel):
    id:int
    content: str
    replies : Optional[list['Comment']] = None

Comment.model_rebuild()  

comment = Comment(
    id=101,
    content="test",
    replies=[
        Comment(id = 102, content="test_reply", replies=[
            Comment(id = 103 , content="test_reply_reply")
        ])
    ]
)

print(comment)