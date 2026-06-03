from fastapi import APIRouter
from . import crud

# API router instance, stores all the API endpoints
router = APIRouter()

# Endpoints

# get all the sections
@router.get('/sections')
async def get_sections():
  return crud.get_sections()

# get all folders
@router.get('/folders')
async def get_folders():
  return crud.get_folders()

# get all the posts for the homepage
@router.get('/posts')
async def get_posts():
  return crud.get_posts()