with open('referat.txt', 'r', encoding='utf-8') as f:
    all_text = f.read()
    print(f'Длина строки: {len(all_text)}')
    print(f'Количество слов: {len(all_text.split())}')
    print(all_text.split())
    all_text = all_text.replace(".", "!")


with open('referat2.txt', 'w', encoding='utf-8') as f2:
    f2.write(all_text)
