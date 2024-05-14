import random, string

def generate_password(length = 12, use_letters = True, use_digits = True, use_symbols = True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
        
    if characters:
        return ''.join(random.choice(characters) for _ in range(length))
    else:
        print("--> Please select atleast one type of character !!")
        
        
ans = 'rpg'
while ans.lower() == 'rpg':
    print('----------------------------------------------------------')
    print("&&&  WELCOME TO THE RANDOM PASSWORD GENERATOR SYSTEM  &&& ")
    print('----------------------------------------------------------')
    length = int(input("Enter the length of the password to be generated : "))
    use_letters = input("Do you want to include LETTERS ? (Y/N) : ").lower() == 'y'
    use_digits = input("Do you want to include DIGITS ? (Y/N) : ").lower() == 'y'
    use_symbols = input("Do you want to include SYMBOLS ? (Y/N) : ").lower() == 'y'

    password = generate_password(length, use_letters, use_digits, use_symbols)
    if password:
        print("\nGenerated Password is ", password)
        print("__/\__ THANK YOU !!")
        print('----------------------------------------------------------')
    else:
        print("\n*** Password generation failed !! ***")
        print("--> Please try again  __/\__")
        print('----------------------------------------------------------')
        
    print()
    ans = input("Type 'rpg/RPG' to run the system again : ")
    print()
    print()