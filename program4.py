def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in text:
        if char.isalpha(): 
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count
user_input = input("Enter a string: ")
v_count, c_count = count_vowels_consonants(user_input)
print(f"Vowels: {v_count}")
print(f"Consonants: {c_count}")