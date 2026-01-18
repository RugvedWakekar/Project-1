alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import art
print(art.logo)

def caesar(original_text, shift_amount, encode_or_decode):
    cipher_text = ""
    if encode_or_decode == "decode":
       shift_amount *= -1

       for each_letter in original_text:
           shifted_position = alphabet.index(each_letter) + shift_amount
           shifted_position %= len(alphabet)
           cipher_text += alphabet[shifted_position]
       print(f"Here is your {encode_or_decode}d result: {cipher_text}")

    