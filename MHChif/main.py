from Decryption import Decryption
from  Encryption import Encryption

def main():
    print("# =========== Encryption =========== #")
    merkle_hellman = Encryption()
    merkle_hellman.read_user_input()

    print("\n# =========== Decryption =========== #")
    merkle_hellman_dec = Decryption(merkle_hellman.w, merkle_hellman.q, merkle_hellman.r,
                                    merkle_hellman.encrypted_text)
    merkle_hellman_dec.decrypt()

if __name__ == '__main__':
    main()