file_path = "../resource/word/demo1.txt"
file_path = "log/demo.log"
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
