from fastapi import APIRouter
from ..crud import contribution as c
from ..schemas import ContributionCreate, ContributionResponse, ContributionStatusUpdate

router = APIRouter()

@router.post('/contributions')
async def create_contribution(contrib: ContributionCreate) -> dict:
  return c.create_contribution(contrib.post_id, contrib.suggested_content, contrib.issue)

@router.get('/contributions/{post_id}')
async def get_contributions(post_id: int) -> list[ContributionResponse]:
  return c.get_contributions(post_id)

@router.put('/contributions/{contribution_request_id}')
async def update_contribution(contribution_request_id: int, update: ContributionStatusUpdate) -> dict:
  return c.update_contribution_status(contribution_request_id, update.status)