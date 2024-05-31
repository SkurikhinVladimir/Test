from fastapi import FastAPI
from pydantic import BaseModel
from algorithms import binary_search, merge_sort, palindrome_check
from schemas import BinarySearchInput, MergeSortInput, PalindromeCheckInput

app = FastAPI()

@app.post("/binary_search")
def perform_binary_search(input_data: BinarySearchInput):
    index = binary_search.binary_search(input_data.arr, input_data.target)
    return {"index": index}

@app.post("/merge_sort")
def perform_merge_sort(input_data: MergeSortInput):
    sorted_arr = merge_sort.merge_sort(input_data.arr)
    return {"sorted_array": sorted_arr}

@app.post("/palindrome_check")
def perform_palindrome_check(input_data: PalindromeCheckInput):
    is_palindrome = palindrome_check.is_palindrome(input_data.s)
    return {"is_palindrome": is_palindrome}
