letter = '''Dear <|Name|>,
You are selected!
<|Date|> '''
print(letter)
print(letter.replace("<|Name|>","Umer").replace("<|Date|>", "13-Jun-2025"))