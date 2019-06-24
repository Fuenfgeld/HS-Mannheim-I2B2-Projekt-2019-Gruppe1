
stringList = ['abc', 'def', 'ghi', 'jkl', 'mno']
abcd = 'abcd'
logic_or = 'or'

def replace_slash(string):
    print(string)
    string = string.replace('\\', '_')
    print(string)
    return string

print(replace_slash('slash\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\killa'))