import os

class Config:
    DEBUG = True
    FILE_PATH = os.getenv('FILE_PATH')
