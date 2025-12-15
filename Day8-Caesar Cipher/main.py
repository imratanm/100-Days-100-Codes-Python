alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

work = input("Enter encode for Encrption and decode for Decryption: ").lower()
shift_times = int(input("Enter shift times: " ))

def ceaser(shift , direction):

    if direction == "encode":
        text = input("Enter the data : ").lower()
        encrypted_text = ""
        for i in text:
            shifted_position = alphabet.index(i) + shift
            shifted_position %= len(alphabet) 
            encrypted_text += alphabet[shifted_position]

        print(f"Here is your encrypted text {encrypted_text}")

    elif direction == "decode":
        text = input("Enter the data : ").lower()
        decrypted_text = ""
        for i in text:
            shifted_position = alphabet.index(i) - shift
            shifted_position %= len(alphabet)
            decrypted_text += alphabet[shifted_position]

        print(f"Here is your decrypted text : {decrypted_text}")

    else:
        print("Wrong input! Please input encode or decode.")


ceaser(shift=shift_times, direction= work )