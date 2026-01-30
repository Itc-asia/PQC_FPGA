from pqcrypto.kem import ml_kem_512
from dilithium_py.dilithium import Dilithium2


def xor_encrypt(message: bytes, key: bytes) -> bytes:
    key_stream = key * (len(message) // len(key) + 1)
    return bytes(m ^ k for m, k in zip(message, key_stream))


def save_bytes(filename: str, data: bytes):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(data.hex())


def load_bytes(filename: str) -> bytes:
    with open(filename, "r", encoding="utf-8") as f:
        return bytes.fromhex(f.read().strip())


def load_text(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    # ===== 明文（bytes）=====
    message = load_text("6.txt").encode("utf-8")

    # ===== 读取共享密钥 =====
    shared_secret = load_bytes("shared_secret.txt")

    # ===== 读取签名密钥 =====
    sk = load_bytes("sk.txt")

    # ===== 对信息进行签名 =====
    signature = Dilithium2.sign(sk, message)
    print("数字签名已完成!")

    # ===== 对称加密 =====
    ciphertext_msg = xor_encrypt(message, shared_secret)

    # ===== 保存结果 =====
    save_bytes("ciphertext_msg.txt", ciphertext_msg)
    save_bytes("signature.txt", signature)

    print("量子加密已经完成!")
