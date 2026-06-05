from .db import conn
from .schemas import SectionResponse, FolderResponse, PostResponse, PostCreate, NoteResponse
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
  
  # close cursor
  cursor.close()

  # return json
  return response

# return all folders
def get_folders():
  # create a cursor to execute SQL
  cursor = conn.cursor()
  cursor.execute("SELECT folder_id, section_id, user_id, name, description, slug, created_at, updated_at FROM folders")


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

  # close cursor
  cursor.close()

  # return json
  return response

# return all the posts
def get_posts():
  # create a cursor to execute SQL
  cursor = conn.cursor()
  cursor.execute("SELECT post_id, folder_id, user_id, title, content, created_at, updated_at FROM posts")

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

  # close cursor
  cursor.close()

  return response

# create a post
def create_post(post):
  # create a cursor to execute SQL
  cursor = conn.cursor()

  # execute sql query (RETURNING immediately returns the inserted row instead of separate search)
  cursor.execute(
    """
      INSERT INTO posts(user_id, folder_id, title, content)
      VALUES (%s, %s, %s, %s)
      RETURNING post_id
    """,
    (1, post.folder_id, post.title, post.content)
  )
  # store returned tuple
  row = cursor.fetchone()
  post_id = row[0]

  # permanently save changes to DB and close
  conn.commit()
  cursor.close()

  return {"post_id": post_id}

# update a post
def update_post(post_id, post):
  # create a cursor to execute SQL
  cursor = conn.cursor()

  # execute sql query (RETURNING immediately returns the inserted row instead of separate search)
  cursor.execute(
    """
      UPDATE posts
      SET title = %s, content = %s, updated_at = NOW()
      WHERE post_id = %s AND user_id = %s
      RETURNING post_id
    """,
    (post.title, post.content, post_id, 1)
  )
  # store returned tuple
  row = cursor.fetchone()

  if row is None:
    conn.commit()
    cursor.close()
    return {"error": "Post not found or unauthorized"}

  post_id = row[0]
  # permanently save changes to DB and close
  conn.commit()
  cursor.close()

  return {"post_id": post_id}

# delete a post
def delete_post(post_id):
  # create a cursor to execute sql
  cursor = conn.cursor()

  # execute sql query
  cursor.execute(
    """
      DELETE FROM posts
      WHERE post_id = %s AND user_id = %s
      RETURNING post_id
    """,
    (post_id, 1)
  )
  # store returned tuple
  row = cursor.fetchone()

  if row is None:
    conn.commit()
    cursor.close()
    return {"error": "Post not found or unauthorized"}
  
  post_id = row[0]
  # permanently save changes to DB and close
  conn.commit()
  cursor.close()

  return {"message": "Post deleted successfully"}

# create a folder
def create_folder(folder):
  # create a cursor to execute SQL
  cursor = conn.cursor()

  # execute sql query (RETURNING immediately returns the inserted row instead of separate search)
  cursor.execute(
    """
      INSERT INTO folders(user_id, section_id, name, description, slug)
      VALUES(%s, %s, %s, %s, %s)
      RETURNING folder_id
    """,
    (1, folder.section_id, folder.name, folder.description, folder.slug)
  )
  # store returned tuple
  row = cursor.fetchone()
  folder_id = row[0]

  # permanently save changes to DB and close
  conn.commit()
  cursor.close()

  return {"folder_id": folder_id}

# update a folder
def update_folder(folder_id, folder):
  cursor = conn.cursor()
  
  cursor.execute(
    """
      UPDATE folders
      SET name = %s, description = %s, slug = %s, updated_at = NOW()
      WHERE folder_id = %s AND user_id = %s
      RETURNING folder_id
    """,
    (folder.name, folder.description, folder.slug, folder_id, 1)
  )
  row = cursor.fetchone()
  
  if row is None:
    conn.commit()
    cursor.close()
    return {"error": "Folder not found or unauthorized"}
  
  conn.commit()
  cursor.close()
  return {"folder_id": row[0]}

# delete a folder
def delete_folder(folder_id):
  # create a cursor to execute sql
  cursor = conn.cursor()

  # execute sql query
  cursor.execute(
    """
      DELETE FROM folders
      WHERE folder_id = %s AND user_id = %s
      RETURNING folder_id
    """,
    (folder_id, 1)
  )
  # store returned tuple
  row = cursor.fetchone()

  if row is None:
    conn.commit()
    cursor.close()
    return {"error": "Folder not found or unauthorized"}
  
  folder_id = row[0]
  # permanently save changes to DB and close
  conn.commit()
  cursor.close()

  return {"message": "Folder deleted successfully"}

# create a personal note
def create_note(note):
  # create a cursor to execute SQL
  cursor = conn.cursor()

  # execute sql query (RETURNING immediately returns the inserted row instead of separate search)
  cursor.execute(
    """
      INSERT INTO notes(user_id, post_id, body)
      VALUES(%s, %s, %s)
      RETURNING note_id
    """,
    (1, note.post_id, note.body)
  )
  # store returned tuple
  row = cursor.fetchone()
  note_id = row[0]

  # permanently save changes to DB and close
  conn.commit()
  cursor.close()

  return {"note_id": note_id}

# update a personal note
def update_note(note_id, note):
  # create a cursor to execute SQL
  cursor = conn.cursor()

  # execute sql query (RETURNING immediately returns the inserted row instead of separate search)
  cursor.execute(
    """
      UPDATE notes
      SET body = %s, updated_at = NOW()
      WHERE note_id = %s AND user_id = %s
      RETURNING note_id 
    """,
    (note.body, note_id, 1)
  )
  # store returned tuple
  row = cursor.fetchone()

  if row is None:
    conn.commit()
    cursor.close()
    return {"error": "Note not found or unauthorized"}

  note_id = row[0]
  # permanently save changes to DB and close
  conn.commit()
  cursor.close()

  return {"note_id": note_id}

# delete a personal note
def delete_note(note_id):
  # create a cursor to execute SQL
  cursor = conn.cursor()

  # execute sql query (RETURNING immediately returns the inserted row instead of separate search)
  cursor.execute(
    """
      DELETE FROM notes
      WHERE note_id = %s AND user_id = %s
      RETURNING note_id
    """,
    (note_id, 1)
  )
  # store returned tuple
  row = cursor.fetchone()

  if row is None:
    conn.commit()
    cursor.close()
    return {"error": "Note not found or unauthorized"}

  note_id = row[0]
  # permanently save changes to DB and close
  conn.commit()
  cursor.close()

  return {"message": "Note deleted successfully"}

# return a personal note
def get_notes(post_id):
  # create a cursor to execute SQL
  cursor = conn.cursor()

  # execute sql query (RETURNING immediately returns the inserted row instead of separate search)
  cursor.execute(
    """
      SELECT note_id, body, created_at 
      FROM notes
      WHERE post_id = %s AND user_id = %s
    """,
    (post_id, 1)
  )

  # fetch query result as a list of tuples
  notes = cursor.fetchall()

  # convert list to FolderResponse pydantic object 
  response = list()
  for row in notes:
    note = NoteResponse(
      note_id = row[0],
      body = row[1],
      created_at = row[2]
    )
    response.append(note)

  # close cursor
  cursor.close()
  
  return response

