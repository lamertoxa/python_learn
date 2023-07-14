def pretty_message(data):
    import re
    a = re.sub(r'(\w+?)\1+(\w){1,}' ,r'\1',data)
    return a

print (pretty_message("True"))
