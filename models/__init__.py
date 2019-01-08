#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""

import os

if 'HBNB_TYPE_STORAGE' in os.environ.keys():
    if os.environ['HBNB_TYPE_STORAGE'] == 'db':
        from models.engine.db_storage import DBStorage
        storage = DBStorage()
        storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
