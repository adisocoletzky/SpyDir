import subprocess

WHITESPACE = ''.join(chr(i) for i in [32, 9, 10, 13, 11, 12])
WINMERGE_PATH = r'"C:\Program Files (x86)\WinMerge\WinMergeU.exe"'
PARAMS = '-cfg Font/Height = 32 -cfg Font/FaceName = MS Mincho -cfg Font/Underline = 1'
file_1_path = r'E:\cyber_test\adi.txt'
file_2_path = r'E:\cyber_test\adighj.txt'
file_3_path = WHITESPACE

# command = f'cmd /k {WINMERGE_PATH} {file_1_path} {file_2_path} {file_3_path}'
command = f'cmd /k {WINMERGE_PATH} {file_1_path} {file_2_path} {file_3_path} {PARAMS}'
subprocess.Popen(command)
