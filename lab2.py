# Алфавит для шифра Виженера
ALPHABET = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '
DEFAULT_SHIFT = -3

print('Используем шифр Виженера для русского алфавита и пробела\n')
original_text = input('Введите сообщение: ')
encryption_key = input('Введите ключ: ')
encryption_key *= (len(original_text) // len(encryption_key)) + 1  # расширение ключа до длины сообщения
print('Исходный текст: ' + original_text)
print('Ключ: ' + encryption_key + '\n')

encrypted_text = ''
for idx in range(len(original_text)):
    char = original_text[idx]
    shift_amt = (ALPHABET.find(encryption_key[idx]) + 1) % len(ALPHABET)
    index = ALPHABET.find(char)
    adjusted_index = index + shift_amt - len(ALPHABET)
    if shift_amt > 0 and adjusted_index >= 0:
        encrypted_text += ALPHABET[adjusted_index]
    elif shift_amt < 0 and adjusted_index < -len(ALPHABET):
        encrypted_text += ALPHABET[len(ALPHABET) + index + shift_amt]
    else:
        encrypted_text += ALPHABET[index + shift_amt]
print('Зашифрованный текст: ' + encrypted_text + '\n')

decrypted_text = ''
for idx in range(len(encrypted_text)):
    char = encrypted_text[idx]
    shift_amt = (ALPHABET.find(encryption_key[idx]) + 1) % len(ALPHABET)
    index = ALPHABET.find(char)
    adjusted_index = index - shift_amt - len(ALPHABET)
    if -shift_amt > 0 and adjusted_index >= 0:
        decrypted_text += ALPHABET[adjusted_index]
    elif -shift_amt < 0 and adjusted_index < -len(ALPHABET):
        decrypted_text += ALPHABET[len(ALPHABET) + index - shift_amt]
    else:
        decrypted_text += ALPHABET[index - shift_amt]
print('Расшифрованный текст: ' + decrypted_text)
