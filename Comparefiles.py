import difflib
before=''
after=''
def comparefiles(after,before):
    with open(before, mode='r') as f:
        all_lines_before = f.readlines()
    with open(after, mode='r') as f:
        all_lines_after = f.readlines()
    output_list = [li for li in difflib.ndiff(str(all_lines_before), str(all_lines_after)) if li[0] != ' ']
    for ch in output_list:
        print(ch[2], end='')
    print('')
