from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(text, shift, direction):
        shift = int(shift)%26
        new_text = ''
        for i in range(len(text)):
            if text[i].isalpha():
                if direction == 'encode':
                    new_index = alphabet.index(text[i]) + shift
                else:
                    new_index = alphabet.index(text[i]) - shift
                new_text += alphabet[new_index]
            else:
                new_text += text[i]
        print(f"The {direction}d text is {new_text}")

    caesar(text, shift, direction)
    if input("Type 'yes' if you want to go again. Otherwise type 'no'\n") == 'no':
        print("Bye, bye")
        break
