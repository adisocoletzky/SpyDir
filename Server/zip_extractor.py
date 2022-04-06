import zipfile


def extract_zip(zip_path, dest_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_file:
        zip_file.extractall(dest_path)
