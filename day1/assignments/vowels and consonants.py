def count(word):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for i in word:
        if i.isalpha():
            if i in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

a = input("Enter a string: ")
vowels, consonants = count(a)

print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")