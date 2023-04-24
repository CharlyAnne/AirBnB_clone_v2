#!/usr/bin/python3
'''The Package initializer'''
import os

type_storage = os.getenv('HBNB_TYPE_STORAGE')

def storage_mode():
    """Define storage mode based on os.environ"""
    st_mode = os.getenv('HBNB_TYPE_STORAGE', default='file')

    def is_db():
        """Check if the storage type is a database"""
        if st_mode == 'db':
            return True
        return False
    return is_db()
if not storage_mode():
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

else:
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
    

if type_storage == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()


if __name__ == '__main__':
    storage_mode()


