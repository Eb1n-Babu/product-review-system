# test_env.py
import os
from dotenv import load_dotenv

load_dotenv()
print("DJANGO_SECRET_KEY:", os.getenv('DJANGO_SECRET_KEY'))