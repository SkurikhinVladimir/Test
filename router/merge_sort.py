from fastapi import APIRouter
from schemas import MergeSortInput
from algorithms import merge_sort

router = APIRouter()

@router.post("/")
def perform_merge_sort(input_data: MergeSortInput):
    sorted_arr = merge_sort.merge_sort(input_data.arr)
    return {"sorted_array": sorted_arr}
