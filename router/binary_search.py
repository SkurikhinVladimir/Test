from fastapi import APIRouter
from schemas import BinarySearchInput
from algorithms import binary_search

router = APIRouter()

@router.post("/")
def perform_binary_search(input_data: BinarySearchInput):
    index = binary_search.binary_search(input_data.arr, input_data.target)
    return {"index": index}
