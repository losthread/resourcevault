from .db import conn
from .schemas import SectionResponse, FolderResponse, PostResponse
from datetime import datetime

# return all the sections
def get_sections():
  # create a cursor to execute SQL
  cursor = conn.cursor()
  cursor.execute("SELECT section_id, name, description, slug, created_at FROM sections")

  # fetch query result as a list of tuples
  sections = cursor.fetchall()

  # convert list to SectionResponse pydantic object 
  response = list()
  for row in sections:
    section = SectionResponse(
      section_id = row[0],
      name = row[1],
      description = row[2],
      slug = row[3],
      created_at = row[4]
    )
    response.append(section)
  
  # return json
  return response

# return all folders
def get_folders():
  # create a cursor to execute SQL
  cursor = conn.cursor()
  cursor.execute("SELECT post_id, folder_id, user_id, title, content, created_at, updated_at FROM posts")


  # fetch query result as a list of tuples
  folders = cursor.fetchall()

  # convert list to FolderResponse pydantic object 
  response = list()
  for row in folders:
    folder = FolderResponse(
      folder_id=row[0],
      section_id=row[1],
      user_id=row[2],
      name=row[3],
      description=row[4],
      slug=row[5],
      created_at=row[6],
      updated_at=row[7]
    )
    response.append(folder)

  # return json
  return response

# return all the posts
def get_posts():
  # create a cursor to execute SQL
  cursor = conn.cursor()
  cursor.execute("SELECT post_id, folder_id, title, content, created_at, updated_at FROM posts")

  # fetch query result as a list of tuples
  posts = cursor.fetchall()

  # convert list to FolderResponse pydantic object 
  response = list()
  for row in posts:
    post = PostResponse(
      post_id=row[0],
      folder_id=row[1],
      user_id=row[2],
      title=row[3],
      content=row[4],
      created_at=row[5],
      updated_at=row[6]
    )
    response.append(post)

  return response

