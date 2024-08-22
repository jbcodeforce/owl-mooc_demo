import unittest
from dotenv import load_dotenv
import sys,os
os.environ["CONFIG_FILE"] = "./tests/ut/config/config.yaml"
from dotenv import load_dotenv
load_dotenv("./.env")
sys.path.append('./src')
from main import app
from app_settings import get_config
from fastapi.testclient import TestClient


class TestPromptApi(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.client = TestClient(app)
        print("init test done")
       

    def test_get_student_by_id(self):
        print("\ntest_get_default_prompt\n")
        response = self.client.get(get_config().api_route +"/students/S1")
        print(f"\n--it--> {response.json()}")
        assert response is not None
        assert response.status_code == 200
        assert "S1" in response.json()["student_id"]
