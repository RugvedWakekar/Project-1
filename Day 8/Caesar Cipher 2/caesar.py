alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(original_text, shift_amount, encode_or_decode):
    cipher_text = ""
    for each_letter in original_text:

        if encode_or_decode  == "decode":
            shift_amount *= -1

        shifted_positon = alphabet.index(each_letter) + shift_amount #it is saved as integer
        shifted_positon %= len(alphabet)
        cipher_text += alphabet[shifted_positon] #here that integer stored index of the alphabet
    print(f"Here is your {encode_or_decode}d result: {cipher_text}")
caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
exit()




