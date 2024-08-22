
import json
from app_settings import get_config
from pydantic import BaseModel
import uuid
from functools import lru_cache


class Student(BaseModel): 
    student_id: str = str(uuid.uuid4())
    name: str = ""
    gender: str = ""
    age: int = 18
    major: str = "Computer Science"
    graduation_date: str = ""

class StudentManager():
    """
    The student manager manages Student Entities.
    """
    
    def __init__(self):
        self.STUDENTS: dict = dict()

    def get_student_by_id(self, id: str) -> Student:
        """
        Get Student entity description given its unique identifier
        Args:
            id (str): unique identifier persisted as student_id

        Returns:
            OwlAssistantEntity: The assistant entity with information to create instance of the assistant with one to many agents
        """
        return self.STUDENTS[id]
    
    def load_students(self, path: str):
        """ Load all the assistants definition from the file systems"""
        with open(path, "r", encoding="utf-8") as f:
            a_dict = json.load(f)  # a dict with assistant entities
            print(a_dict)
            for oa in a_dict:
                oae=Student.model_validate(oa)
                self.STUDENTS[oae.student_id]=oae


_instance = None

@lru_cache
def get_student_manager() -> StudentManager:
    """ Factory to get access to unique instance of assistant manager"""
    global _instance
    if _instance is None:
        path = get_config().data_path
        if path is None:
            path="./students.json"
        _instance = StudentManager()
        _instance.load_students(path)
    return _instance