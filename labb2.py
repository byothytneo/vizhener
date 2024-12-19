import itertools 
from collections import Counter 

ALPHABET = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
EXPECTED_FREQUENCY = { 
    'О': 0.1097, 'Е': 0.0845, 'А': 0.0801, 'И': 0.0735, 'Н': 0.067, 'Т': 0.0626, 'С': 0.0547, 'Р': 0.0473, 'В': 0.0454, 'Л': 0.0434, 'К': 0.0349, 'М': 0.0321, 
    'Д': 0.0298, 'П': 0.0281, 'У': 0.0262, 'Я': 0.0201, 'Ы': 0.019, 'З': 0.0165, 'Б': 0.0159, 'Г': 0.0133, 'Ч': 0.0122, 'Й': 0.0104, 'Х': 0.0097, 'Ж': 0.0094, 
    'Ш': 0.0073, 'Ю': 0.0064, 'Ц': 0.0048, 'Щ': 0.0036, 'Э': 0.0032, 'Ф': 0.0026, 'Ъ': 0.0004, 'Ь': 0.0174 
}

def calc_freq(text): 
    text = text.replace(' ', '').upper() 
    counter = Counter(text) 
    total = sum(counter.values()) 
    freq = {char: count / total for char, count in counter.items()} 
    return freq 

def index_of_coincidence(text): 
    text = text.replace(' ', '').upper() 
    counter = Counter(text) 
    total = sum(counter.values()) 
    ic = sum(count * (count - 1) for count in counter.values()) / (total * (total - 1)) 
    return ic 

def encrypt_vigenere(original_text, encryption_key):
    encryption_key *= (len(original_text) // len(encryption_key)) + 1
    encrypted_text = ''
    for idx in range(len(original_text)):
        char = original_text[idx]
        if char in ALPHABET:
            shift_amt = (ALPHABET.find(encryption_key[idx]) + 1) % len(ALPHABET)
            index = ALPHABET.find(char)
            adjusted_index = (index + shift_amt) % len(ALPHABET)
            encrypted_text += ALPHABET[adjusted_index]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_vigenere(encrypted_text, encryption_key):
    encryption_key *= (len(encrypted_text) // len(encryption_key)) + 1
    decrypted_text = ''
    for idx in range(len(encrypted_text)):
        char = encrypted_text[idx]
        if char in ALPHABET:
            shift_amt = (ALPHABET.find(encryption_key[idx]) + 1) % len(ALPHABET)
            index = ALPHABET.find(char)
            adjusted_index = (index - shift_amt) % len(ALPHABET)
            decrypted_text += ALPHABET[adjusted_index]
        else:
            decrypted_text += char
    return decrypted_text

def encrypt_text(text, shift):
    return ''.join([ALPHABET[(ALPHABET.find(char) + shift) % len(ALPHABET)] if char in ALPHABET else char for char in text])

def decrypt_text(text, shift):
    return ''.join([ALPHABET[(ALPHABET.find(char) - shift) % len(ALPHABET)] if char in ALPHABET else char for char in text])


def crack_vizhener_cipher(input_text): 
    possible_keys = [] 
    for key_len in range(1, 21): 
        substrings = [''.join(input_text[i::key_len]) for i in range(key_len)] 
        avg_ic = sum(index_of_coincidence(sub) for sub in substrings) / key_len 
        if abs(avg_ic - 0.055) < 0.01:
            possible_keys.append(key_len)

    for key_len in possible_keys: 
        key = [] 
        for i in range(key_len): 
            substr = ''.join(input_text[j] for j in range(i, len(input_text), key_len)) 
            freq = calc_freq(substr) 
            key_char = max(freq, key=lambda x: freq[x] / EXPECTED_FREQUENCY.get(x, 0)) 
            key.append(key_char)

        key = ''.join(key) 
        decrypted_text = decrypt_vigenere(input_text, key)
        return key, decrypted_text

def main():
    print('Шифр Виженера')
    action = input("Выберите действие:\n1 - Зашифровать\n2 - Дешифровать\n3 - Взломать\nВведите номер действия: ")
    
    if action not in ['1', '2', '3']:
        print("Неверный ввод. Пожалуйста, выберите 1, 2 или 3.")
        return

    if action == '1':
        original_text = input('Введите сообщение: ')
        encryption_key = input('Введите ключ: ')
        encrypted_text = encrypt_vigenere(original_text, encryption_key)
        print('Исходный текст: ' + original_text)
        print('Зашифрованный текст: ' + encrypted_text + '\n')
        
    elif action == '2':
        original_text = input('Введите сообщение: ')
        decryption_key = input('Введите ключ: ')
        decrypted_text = decrypt_vigenere(original_text, decryption_key)
        print('Исходный текст: ' + original_text)
        print('Расшифрованный текст: ' + decrypted_text)

    elif action == '3':
        input_text = input('Введите зашифрованное сообщение для взлома: ')
        key, decrypted_text = crack_vizhener_cipher(input_text)
        print('Найденный ключ: ' + key)
        print('Расшифрованный текст: ' + decrypted_text)

if __name__ == "__main__":
    main()
