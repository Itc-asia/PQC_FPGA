from pqcrypto.kem import ml_kem_512
from dilithium_py.dilithium import Dilithium2
def xor_crypt(data: bytes, key: bytes) -> bytes:
    key_stream = key * (len(data) // len(key) + 1)
    return bytes(d ^ k for d, k in zip(data, key_stream))


def load_bytes(filename):
    with open(filename, "rb") as f:
        return f.read()


def save_bytes(filename, data):
    with open(filename, "wb") as f:
        f.write(data)

def load_bytes_txt(filename: str) -> bytes:
    with open(filename, "r", encoding="utf-8") as f:
        return bytes.fromhex(f.read().strip())

def save_bytes_txt(filename: str, data: bytes):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(data.hex())

if __name__ == "__main__":
    # ===== 读取图片 =====
    image_data = load_bytes("7.jpg")

    # ===== 加载共享密钥 =====
    shared_secret = bytes.fromhex(open("shared_secret.txt").read().strip())

    # ===== 读取签名密钥 =====
    sk = load_bytes_txt("sk.txt")

    # ===== 对信息进行签名 =====
    signature = Dilithium2.sign(sk, image_data)
    print("图片签名完成!")

    # ===== 加密 =====
    ciphertext = xor_crypt(image_data, shared_secret)

    # ===== 保存密文图片 =====
    save_bytes("cipher_image.bin", ciphertext)
    save_bytes_txt("signature.txt", signature)
    print("图片加密完成!")
