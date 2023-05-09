from cryptography.fernet import Fernet

message= input("Please input a string: ")

key = Fernet.generate_key()
fernet = Fernet(key)

cryptMessage = fernet.encrypt(message.encode())
decryptMessage = fernet.decrypt(cryptMessage).decode()

key = {
    "A": "M",
    "B": "L",
    "C": "K",
    "D": "J",
    "E": "L",
    "F": "H",
    "G": "G",
    "H": "F",
    "I": "E",
    "J": "D",
    "K": "C",
    "L": "B",
    "M": "A",
    "N": "Z",
    "O": "Y",
    "P": "X",
    "Q": "W",
    "R": "V",
    "S": "U",
    "T": "T",
    "U": "S",
    "V": "R",
    "W": "Q",
    "X": "P",
    "Y": "O",
    "Z": "N",
    " ": " "
}


def message_enc(key, string):
    message_array = []
    message_array[:0] = string.upper()
    for _ in message_array:
        print(key[_], end="")


print(f"\nOriginal Message: {message}\n")
print(f"Encrypted Message:", end=" ")
message_enc(key, message)
print(f"\nBetter Encryption Method: {cryptMessage}")
print(f"\nDecrypted Messgae: {message}")

