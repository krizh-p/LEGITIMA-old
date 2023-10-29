# Import the hashlib and Crypto modules
import hashlib
import Crypto.Cipher.AES

# Define a function that takes a password and a message as inputs and returns an encrypted message
def encrypt(password, message):
  # Hash the password using SHA-256 and get the first 16 bytes as the key
  key = hashlib.sha256(password.encode()).digest()[:16]
  # Create an AES object with the key and a random initialization vector (IV)
  iv = Crypto.Random.get_random_bytes(16)
  aes = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_CBC, iv)
  # Pad the message with spaces to make it a multiple of 16 bytes
  padded_message = message + " " * (16 - len(message) % 16)
  # Encrypt the padded message using AES and concatenate the IV and the ciphertext
  ciphertext = aes.encrypt(padded_message.encode())
  encrypted_message = iv + ciphertext
  # Return the encrypted message
  return encrypted_message

# Define a function that takes a password and an encrypted message as inputs and returns a decrypted message
def decrypt(password, encrypted_message):
  # Hash the password using SHA-256 and get the first 16 bytes as the key
  key = hashlib.sha256(password.encode()).digest()[:16]
  # Split the encrypted message into the IV and the ciphertext
  iv = encrypted_message[:16]
  ciphertext = encrypted_message[16:]
  # Create an AES object with the key and the IV
  aes = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_CBC, iv)
  # Decrypt the ciphertext using AES and strip the padding spaces
  padded_message = aes.decrypt(ciphertext).decode()
  message = padded_message.strip()
  # Return the decrypted message
  return message

# Test the functions with some sample input
serializedToken = "mysecretpassword" # The password to use as an input
productInformation = productInformation = """{
    "product_name": "Sample Product",
    "product_id": "123456",
    "manufacturer": "Sample Manufacturer",
    "manufactured_date": "2023-10-25",
    "sold_to_retailer_date": "2023-11-02",
    "retailer": "Sample Retailer Inc.",
    "price": 49.99,
    "currency": "USD",
    "category": "Electronics",
    "color": "Black",
    "weight": "1.2 kg",
    "dimensions": {
        "length": 10.5,
        "width": 5.2,
        "height": 2.0
    },
    "description": "This is a sample product description. It is a high-quality, feature-rich product suitable for various applications.",
    "features": [
        "Wireless connectivity",
        "Long-lasting battery",
        "HD display",
        "Advanced functionality"
    ],
    "warranty": {
        "valid_from": "2023-11-05",
        "valid_to": "2024-11-05",
        "warranty_provider": "Sample Warranty Services"
    }
}"""
#  # The message to encrypt and decrypt
# encrypted_message = encrypt(serializedToken, productInformation) # The encrypted message
# # print(encrypted_message) # Print the output
# decrypted_message = decrypt(serializedToken, encrypted_message) # The decrypted message
# print("decrypted_message:") # Print the output
# print(decrypted_message) # Print the output
