from fastapi import APIRouter, Depends
from ..crud import contribution as c
from ..schemas import ContributionCreate, ContributionResponse, ContributionStatusUpdate
from ..dependencies import get_user_id

router = APIRouter()

@router.post('/contributions')
async def create_contribution(contrib: ContributionCreate, user_id: int = Depends(get_user_id)) -> dict:
  return c.create_contribution(contrib.post_id, contrib.suggested_content, contrib.issue, user_id)

@router.get('/contributions/{post_id}')
async def get_contributions(post_id: int) -> list[ContributionResponse]:
  return c.get_contributions(post_id)

@router.get('/user/contributions')
async def get_contributions_per_user(user_id: int = Depends(get_user_id)) -> list[ContributionResponse]:
  return c.get_contributions_per_user(user_id)

@router.get('/user/contributions/{post_id}')
async def get_contributions_per_user_by_post(post_id: int, user_id: int = Depends(get_user_id)) -> list[ContributionResponse]:
  return c.get_contributions_per_user_by_post(post_id, user_id)

@router.put('/contributions/{contribution_request_id}')
async def update_contribution(contribution_request_id: int, update: ContributionStatusUpdate, user_id: int = Depends(get_user_id)) -> dict:
  return c.update_contribution_status(contribution_request_id, update.status, user_id)