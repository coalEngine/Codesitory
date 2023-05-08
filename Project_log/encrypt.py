from cryptography.fernet import Fernet

message= input("Please input a string: ")

key = Fernet.generate_key()
fernet = Fernet(key)

cryptMessage = fernet.encrypt(message.encode())
decryptMessage = fernet.decrypt(cryptMessage).decode()

key = {
    "A": "M",
    "B": "L",
    "C": "",
    "D": "",
    "E": "",
    "F": "",
    "G": "",
    "H": "",
    "I": "",
    "J": "",
    "K": "",
    "L": "",
    "M": "",
    "O": "",
    "P": "",
    "Q": "",
    "R": "",
    "S": "",
    "T": "",
    "U": "",
    "V": "",
    "W": "",
    "X": "",
    "Y": "",
    "Z": "",
}


def message_enc(key, string):
    message_array = []
    message_array[:0] = string.upper()
    for _ in message_array.index():
        print(key[message_array[_]])


print(f"\nOriginal Message: {message}")
print(f"\nEncrypted Message: {cryptMessage}")
print(f"\nDecrypted Messgae: {decryptMessage}")

message_enc(key, message)