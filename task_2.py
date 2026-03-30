def is_palindrome(text: str) -> bool:
    # Оставляем только буквы, приводим к нижнему регистру
    cleaned = ''.join(char.lower() for char in text if char.isalpha())
    return cleaned == cleaned[::-1]

# Тесты
assert is_palindrome("казак") == True
assert is_palindrome("А роза упала на лапу Азора!") == True
assert is_palindrome("Лёша на полке клопа нашёл") == True
assert is_palindrome("A man, a plan, a canal: Panama") == True
assert is_palindrome("") == True
assert is_palindrome("a") == True
assert is_palindrome("Vladimir") == False