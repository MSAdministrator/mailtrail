import os, pendulum


class Config:

    QUERY = os.environ.get('QUERY', '*')
    CHECK_DURATION = int(os.environ.get('CHECK_DURATION', 1))
    USERNAME = os.environ['USERNAME']
    PASSWORD = os.environ['USERNAME']
    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    TENANT_ID = os.environ.get('TENANT_ID')
    STORAGE_PATH = os.environ.get('STORAGE_PATH', '/mailtrail/data')
