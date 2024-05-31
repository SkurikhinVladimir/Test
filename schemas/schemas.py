from pydantic import BaseModel
from typing import List

class BinarySearchInput(BaseModel):
    arr: List[int]
    target: int

class PalindromeCheckInput(BaseModel):
    s: str
