#!/usr/bin/python3
'''The Package initializer'''

def storage_mode():
    """Define storage mode based on os.environ"""
    import os
    st_mode = os.getenv('HBNB_TYPE_STORAGE', default='file')

    def is_db():
        """Check if the storage type is a database"""
        if st_mode == 'db':
            return True
        return False
    return is_db()


if __name__ == '__main__':
    storage_mode()

if not storage_mode():
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

else:
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
    
