#  write a program fill letter template below name and date

source = '''
    Dear <|Name|>,
    You Are Selected!
    <|Date|>
'''

print(source.replace("<|Name|>","Shubham").replace("<|Date|>","5/12/25"))