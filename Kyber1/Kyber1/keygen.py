# keygen.py
from pqcrypto.kem import ml_kem_512
from dilithium_py.dilithium import Dilithium2

def save_bytes(filename: str, data: bytes):
    """
    将 bytes 数据以 hex 格式保存到 txt 文件
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(data.hex())


if __name__ == "__main__":

    # 生成数据加密公钥 / 私钥
    public_key, secret_key = ml_kem_512.generate_keypair()

    # 生成数字签名公钥 / 私钥
    pk, sk = Dilithium2.keygen()

    # KEM 密钥封装
    kem_ciphertext, shared_secret = ml_kem_512.encrypt(public_key)

    # ===== 保存到当前目录 =====
    save_bytes("public_key.txt", public_key)
    save_bytes("secret_key.txt", secret_key)
    save_bytes("kem_ciphertext.txt", kem_ciphertext)
    save_bytes("shared_secret.txt", shared_secret)
    save_bytes("sk.txt", sk)
    save_bytes("pk.txt", pk)

    print("秘钥生成成功，所有参数已保存到当前目录下的 .txt 文件")