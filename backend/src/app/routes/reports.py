from fastapi import APIRouter
from ..schemas import ReportCreate, ReportResponse
from ..crud import reports as r

router = APIRouter()

# create a report
@router.post('/reports')
async def create_report(report: ReportCreate) -> dict:
  return r.create_report(report.post_id, report.reason)

# get all reports by a user 
@router.get('/reports')
async def get_reports() -> list[ReportResponse]:
  return r.get_reports()

# get all reposts on a single post
@router.get('/posts/{post_id}/reports')
async def get_reports_on_post(post_id: int) -> list[ReportResponse]:
  return r.get_reports_on_post(post_id)