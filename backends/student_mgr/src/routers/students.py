
from app_settings import get_config
from fastapi import APIRouter
from svc.students_svc import get_student_manager, Student


router = APIRouter( prefix= get_config().api_route +"/students")



@router.get("/{id}")
def get_student_entity_by_id(id: str) -> Student:
    return get_student_manager().get_student_by_id(id)