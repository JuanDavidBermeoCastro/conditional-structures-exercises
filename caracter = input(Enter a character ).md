caracter = input("Enter a character: ")

if caracter.isalpha():
    if caracter.isupper():
        print(f"The character '{caracter}' is an uppercase letter.")
    else:
        print(f"The character '{caracter}' is a lowercase letter.")

elif caracter.isdigit():
    print(f"The character '{caracter}' is a number.")

else:
    print(f"The character '{caracter}' is neither a letter nor a number.")