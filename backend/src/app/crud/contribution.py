from ..database import conn
from .exception import handle_error
from ..schemas import ContributionResponse, PostResponse
from fastapi import HTTPException
from datetime import datetime

# create a contribution request
def create_contribution(post_id, suggested_content, issue, user_id):
  cursor = conn.cursor()
  try:
    cursor.execute(
      """
        INSERT INTO contribution_requests(post_id, user_id, suggested_content, issue, status, created_at, updated_at)
        VALUES(%s, %s, %s, %s, 'Pending', NOW(), NOW())
        RETURNING contribution_request_id
      """,
      (post_id, user_id, suggested_content, issue)
    )
    row = cursor.fetchone()
    conn.commit()
    cursor.close()
    return {"contribution_request_id": row[0]}
  
  except Exception as e:
    handle_error(e, cursor)

# get all contributions on a post
def get_contributions(post_id):
  cursor = conn.cursor()
  cursor.execute(
    """
      SELECT cr.contribution_request_id, cr.suggested_content, cr.issue, cr.status, cr.created_at, cr.updated_at, u.user_id, u.username
      FROM contribution_requests cr
      JOIN users u ON cr.user_id = u.user_id
      WHERE cr.post_id = %s
    """,
    (post_id,)
  )
  contributions = cursor.fetchall()
  cursor.close()
  
  response = list()
  for row in contributions:
    contrib = ContributionResponse(
      contribution_request_id=row[0],
      suggested_content=row[1],
      issue=row[2],
      status=row[3],
      created_at=row[4],
      updated_at=row[5],
      user_id=row[6],
      username=row[7]
    )
    response.append(contrib)
  
  return response

# get all contributions by a user
def get_contributions_per_user(user_id):
  cursor = conn.cursor()
  cursor.execute(
    """
      SELECT cr.contribution_request_id, cr.suggested_content, cr.issue, cr.status, cr.created_at, cr.updated_at, u.user_id, u.username
      FROM contribution_requests cr
      JOIN users u ON cr.user_id = u.user_id
      WHERE cr.user_id = %s
    """,
    (user_id,)
  )
  contributions = cursor.fetchall()
  cursor.close()
  
  response = list()
  for row in contributions:
    contrib = ContributionResponse(
      contribution_request_id=row[0],
      suggested_content=row[1],
      issue=row[2],
      status=row[3],
      created_at=row[4],
      updated_at=row[5],
      user_id=row[6],
      username=row[7]
    )
    response.append(contrib)
  
  return response

# get contributions by a user under a post
def get_contributions_per_user_by_post(post_id, user_id):
  cursor = conn.cursor()
  cursor.execute(
    """
      SELECT cr.contribution_request_id, cr.suggested_content, cr.issue, cr.status, cr.created_at, cr.updated_at, u.user_id, u.username
      FROM contribution_requests cr
      JOIN users u ON cr.user_id = u.user_id
      WHERE cr.post_id = %s AND cr.user_id = %s
    """,
    (post_id, user_id)
  )
  contributions = cursor.fetchall()
  cursor.close()
  
  response = list()
  for row in contributions:
    contrib = ContributionResponse(
      contribution_request_id=row[0],
      suggested_content=row[1],
      issue=row[2],
      status=row[3],
      created_at=row[4],
      updated_at=row[5],
      user_id=row[6],
      username=row[7]
    )
    response.append(contrib)
  
  return response

# accept or reject a contribution request
def update_contribution_status(contribution_request_id, status, user_id):
  cursor = conn.cursor()

  try:
    # get contribution details FIRST
    cursor.execute(
      """
        SELECT post_id, suggested_content
        FROM contribution_requests
        WHERE contribution_request_id = %s AND user_id = %s
      """,
      (contribution_request_id, user_id)
    )
    contrib_row = cursor.fetchone()

    if contrib_row is None:
      cursor.close()
      raise HTTPException(status_code=404, detail="Contribution request not found")
    
    post_id = contrib_row[0]
    suggested_content = contrib_row[1]

    # if accepted, update post content
    if status == "Accepted":
      cursor.execute(
        """
          UPDATE posts
          SET content = %s, updated_at = NOW()
          WHERE post_id = %s
          RETURNING post_id, folder_id, user_id, title, content, created_at, updated_at
        """,
        (suggested_content, post_id)
      )
      row = cursor.fetchone()
      updated_post = PostResponse(
        post_id=row[0],
        folder_id=row[1],
        user_id=row[2],
        title=row[3],
        content=row[4],
        created_at=row[5],
        updated_at=row[6]
      )

    # update contribution status
    cursor.execute(
      """
        UPDATE contribution_requests
        SET status = %s, updated_at = NOW()
        WHERE contribution_request_id = %s
      """,
      (status, contribution_request_id)
    )

    conn.commit()
    cursor.close()
    
    if status == "Accepted":
      return {"updated_post": updated_post}
    else:
      return {"contribution_request_status": status}
    
  except HTTPException:
    raise

  except Exception as e:
    cursor.close()
    handle_error(e, cursor)