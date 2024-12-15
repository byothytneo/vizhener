# Шифр Виженера для русского алфавита и пробела

Шифр Виженера - это метод полиалфавитного шифрования, в котором для каждого символа исходного текста используется ключевая фраза. Каждый символ текста шифруется сдвигом на определенное количество позиций, зависящим от соответствующего символа ключа. Эта реализация использует русский алфавит и пробел.

## Как он работает?

- **Определение алфавита**: В коде используется строка, содержащая символы русского алфавита и пробел.
- **Сдвиг по умолчанию**: В этой реализации сдвиг по умолчанию не используется, так как ключ задается пользователем.
- **Шифрование**: Каждый символ входного текста сдвигается на количество позиций, определяемое соответствующим символом ключа.
- **Дешифрование**: Зашифрованный текст сдвигается обратно на количество позиций, определяемое соответствующим символом ключа, для восстановления оригинального текста.

## Подробные шаги:
Настройка алфавита и ключа: Алфавит определяется как строка из символов русского алфавита и пробела. Ключ вводится пользователем и расширяется до длины сообщения.

Ввод пользователя: Пользователь вводит текст для шифрования и ключ.

Шифрование:

Для каждого символа во входном тексте:

Определяется количество сдвигов на основе соответствующего символа ключа.

Находится позиция символа (index) в алфавите.

Вычисляется новое положение с учетом сдвига.

Добавляется полученный символ в encrypted_text.

Дешифрование:

Для каждого символа в зашифрованном тексте:

Определяется количество сдвигов на основе соответствующего символа ключа.

Находится позиция символа (index) в алфавите.

Вычисляется новое положение с учетом сдвига в обратную сторону.

Добавляется полученный символ в decrypted_text.

# Примеры для тестирования

## Пример 1: Текст на русском с положительным сдвигом

**Входные данные:**
- Текст: `привет`
- Ключ: `ключ`

**Ожидаемый результат:**
- Зашифрованный текст: `тймцфю`
- Расшифрованный текст: `привет`

## Пример 2: Текст на русском с ключом длиной больше текста

**Входные данные:**
- Текст: `мир`
- Ключ: `длинныйключ`

**Ожидаемый результат:**
- Зашифрованный текст: `оют`
- Расшифрованный текст: `мир`

## Пример 3: Текст на русском с пробелами

**Входные данные:**
- Текст: `привет мир`
- Ключ: `секрет`

**Ожидаемый результат:**
- Зашифрованный текст: `тнсцдю уыс`
- Расшифрованный текст: `привет мир`

## Пример 4: Текст с повторяющимся ключом

**Входные данные:**
- Текст: `алгоритм`
- Ключ: `код`

**Ожидаемый результат:**
- Зашифрованный текст: `мшщытълг`
- Расшифрованный текст: `алгоритм`

## Пример 5: Длинный текст с коротким ключом

**Входные данные:**
- Текст: `это длинный текст для тестирования`
- Ключ: `ключ`

**Ожидаемый результат:**
- Зашифрованный текст: `элтж иоьпышя плдвп доц чфтмюяшгжя`
- Расшифрованный текст: `это длинный текст для тестирования`

## Пример 6: Ключ содержит пробелы

**Входные данные:**
- Текст: `шифрование`
- Ключ: `к л ю ч`

**Ожидаемый результат:**
- Зашифрованный текст: `ыцюытъпопи`
- Расшифрованный текст: `шифрование`
