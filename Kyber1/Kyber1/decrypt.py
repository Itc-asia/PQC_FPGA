# decrypt.py
from pqcrypto.kem import ml_kem_512
from dilithium_py.dilithium import Dilithium2

def xor_decrypt(ciphertext: bytes, key: bytes) -> bytes:
    key_stream = key * (len(ciphertext) // len(key) + 1)
    return bytes(c ^ k for c, k in zip(ciphertext, key_stream))



def load_bytes(filename: str) -> bytes:
    """
    从 txt 文件中读取 hex 编码的 bytes
    """
    with open(filename, "r", encoding="utf-8") as f:
        return bytes.fromhex(f.read().strip())


if __name__ == "__main__":
    # ===== 从 keygen.py 生成的 txt 文件加载 =====
    secret_key = load_bytes("secret_key.txt")
    kem_ciphertext = load_bytes("kem_ciphertext.txt")
    ciphertext_msg = load_bytes("ciphertext_msg.txt")
    pk = load_bytes("pk.txt")

    # ===== KEM 解封装 =====
    shared_secret = ml_kem_512.decrypt(secret_key, kem_ciphertext)

    # ===== 对称解密 =====
    message = xor_decrypt(ciphertext_msg, shared_secret)

    # ===== 读取并验证签名 =====
    signature = load_bytes("signature.txt")
    is_valid = Dilithium2.verify(pk, message, signature)

    if is_valid:
        print("签名验证成功!")
    else:
        print("签名验证失败!")

    with open("decrypted_message.txt", "w", encoding="utf-8") as f:
        f.write(message.decode("utf-8"))

    print("解密结果:", message)


