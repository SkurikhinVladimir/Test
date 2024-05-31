from fastapi import APIRouter
from schemas import PalindromeCheckInput
from algorithms import palindrome_check

router = APIRouter()

@router.post("/")
def perform_palindrome_check(input_data: PalindromeCheckInput):
    is_palindrome = palindrome_check.is_palindrome(input_data.s)
    return {"is_palindrome": is_palindrome}
