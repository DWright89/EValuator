from pydantic import BaseModel

class OneComparison(BaseModel):
    trim_one_id: int
    trim_two_id: int