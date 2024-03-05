import os


def get_photo_path(photo_name: str):
    return os.path.join(os.path.dirname(__file__), 'photos', photo_name)
