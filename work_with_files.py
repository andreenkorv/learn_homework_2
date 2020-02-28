with open('text.txt', 'w', encoding='utf-8') as f:
    f.write("Привет, мир!")
with open('text.txt', 'a', encoding='utf-8') as f:
    f.write("Привет, мир!\n")
    f.write("Hello\tWorld!!!\n")
with open('text.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.upper()
        print(line.replace("\t", ''))
