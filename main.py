text = input().split()
count = 0
for i in range(len(text)):
    for j in range(1, len(text)):
        if text[i] == text[j] and len(text[i]) >= 4:
            count += 1
        if count >= 3:
            print(f"Слово {text[i]} встречается {count} раз")
            count -= count
        else:
            continue

print(text)