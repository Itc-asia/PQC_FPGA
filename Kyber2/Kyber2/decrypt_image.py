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
    """
    从 txt 文件中读取 hex 编码的 bytes
    """
    with open(filename, "r", encoding="utf-8") as f:
        return bytes.fromhex(f.read().strip())


if __name__ == "__main__":
    # ===== 读取密文 =====
    cipher_data = load_bytes("cipher_image.bin")
    pk = load_bytes_txt("pk.txt")

    # ===== 加载共享密钥 =====
    shared_secret = bytes.fromhex(open("shared_secret.txt").read().strip())

    # ===== 解密 =====
    image_data = xor_crypt(cipher_data, shared_secret)

    # ===== 读取并验证签名 =====
    signature = load_bytes_txt("signature.txt")
    is_valid = Dilithium2.verify(pk, image_data, signature)

    if is_valid:
        print("签名验证成功!")
    else:
        print("签名验证失败!")

    # ===== 保存恢复后的图片 =====
    save_bytes("recovered.jpg", image_data)

    print("图片解密完成!")
