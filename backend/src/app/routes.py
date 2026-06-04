from fastapi import APIRouter
from .schemas import SectionResponse, FolderResponse, PostResponse, PostCreate, FolderCreate, NoteCreate, NoteResponse, NoteUpdate
from . import crud

router = APIRouter()

# get all the sections
@router.get('/sections')
async def get_sections() -> list[SectionResponse]:
  return crud.get_sections()

# get all folders
@router.get('/folders')
async def get_folders() -> list[FolderResponse]:
  return crud.get_folders()

# get all the posts for the homepage
@router.get('/posts')
async def get_posts() -> list[PostResponse]:
  return crud.get_posts()

# create a post (type hint auto validates input using pydantic model)
@router.post('/posts')
async def create_post(post: PostCreate) -> dict:
  return crud.create_post(post)

# create a folder (type hint auto validates input using pydantic model)
@router.post('/folders')
async def create_folder(folder: FolderCreate) -> dict:
  return crud.create_folder(folder)

# create note
@router.post('/notes/{post_id}')
async def create_note(note: NoteCreate) -> dict:
  return crud.create_note(note)