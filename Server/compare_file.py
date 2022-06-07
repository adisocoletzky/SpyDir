import difflib


def compare_files(before, after):
    #find the differnce between two data
    output_list = list(filter(lambda li: li[0] != ' ', difflib.ndiff(before, after)))
    delta = ''
    for ch in output_list:
        delta += str(ch[2])
    delta = delta.strip(' ')
    return delta