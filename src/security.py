from authx import AuthX, AuthXConfig
from dotenv import load_dotenv
import os
import bcrypt
from datetime import timedelta

config = AuthXConfig()
load_dotenv()
config.JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
config.JWT_ACCESS_COOKIE_NAME = "X-Access-Token"
config.JWT_TOKEN_LOCATION = ["cookies"]
config.JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=60)
config.JWT_COOKIE_SECURE = True
config.JWT_COOKIE_SAMESITE = "lax"

security = AuthX(config=config)

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode('utf-8')

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password.encode('utf-8'))