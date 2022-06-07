import glob
import zipfile


def compress_dir(folder_path, zip_path):
    absolute_root_part = folder_path.rstrip('/')
    absolute_root_part = absolute_root_part[:absolute_root_part.rfind('/')]
    dir_files = glob.glob(folder_path + '/**', recursive=True)
    aliases = [fpath[len(absolute_root_part):] for fpath in dir_files]
    root = aliases[0]
    dir_files = dir_files[1:]  # remove root
    aliases = aliases[1:]  # remove root
    aliases = list(map(lambda alias: alias.replace(root, ''), aliases))

    with zipfile.ZipFile(zip_path, mode='w') as zipf:
        for fpath, alias in zip(dir_files, aliases):
            zipf.write(fpath, arcname=alias)