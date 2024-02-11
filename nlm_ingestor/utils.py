import os
import hashlib
from datetime import datetime


def ensure_bool(value):
    if isinstance(value, bool):
        return value
    elif isinstance(value, str):
        value = value.lower()
        if value in ("true", "false"):
            return value == "true"
        elif value.isdigit():
            return value != "0"
    raise ValueError(f"Can not cast {type(value)}:'{value}' to boolean")


def get_file_sha256(filepath):
    """Calculates the SHA256 hash of the file contents
    :param filepath:
    :return:
    """
    sha2 = hashlib.sha256()
    with open(filepath, "rb") as fh:
        buf_size = 131072  # 128kb
        while True:
            data = fh.read(buf_size)
            if not data:
                break
            sha2.update(data)
    return sha2.hexdigest()


def extract_file_properties(filepath):
    if filepath.endswith(".md"):
        mime_type = "text/x-markdown"
    elif filepath.endswith(".html"):
        mime_type = "text/html"
    elif filepath.endswith(".pdf"):
        mime_type = "application/pdf"
    elif filepath.endswith(".xml"):
        mime_type = "text/xml"
    else:
        mime_type = magic.from_file(filepath, mime=True)
    file_size = os.path.getsize(filepath)
    checksum = get_file_sha256(filepath)
    creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {
        "fileSize": file_size,
        "mimeType": mime_type,
        "checksum": checksum,
        "createdOn": creation_date,
        "isDeleted": False,
    }