"""
App configuration
"""
import os

SECRET_KEY = os.environ.get('SECRET_KEY', 'some_secret_key')

# Name of the folder where local shared files are located
SHARED_FILES_FOLDER_NAME = "files"
