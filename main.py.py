from fastapi import FastAPI
import json

from routers import binary_search, merge_sort, palindrome_check

# Load configuration
with open("config.json") as config_file:
    config = json.load(config_file)

app = FastAPI(
    title=config["app_name"],
    version=config["version"],
    description=config["description"]
)

# Include routers
app.include_router(binary_search.router, prefix="/binary_search", tags=["Binary Search"])
app.include_router(palindrome_check.router, prefix="/palindrome_check", tags=["Palindrome Check"])
