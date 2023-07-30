import os


def checkAuth(key):
    if (key == os.getenv('GIDEON_API_KEY')):
        return True
    return False
