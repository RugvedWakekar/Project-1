

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import art
print(art.logo)

def caesar(original_text, shift_amount, encode_or_decode):
    cipher_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_num = alphabet.index(letter) + shift_amount
            shifted_num %= len(alphabet)
            cipher_text += alphabet[shifted_num]
    print(f"Here is your {encode_or_decode}d result: {cipher_text}\n")

should_continue = True
while should_continue:
    direction  = input("Type 'encode' for encoding or type 'decode' for decoding: \n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type your shift amount: \n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' to start again. Otherwise type 'no'.: \n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye beach")
exit()