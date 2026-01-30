# 📘 Post-Quantum Hybrid Encryption Experiment (ML-KEM)

## 1. 项目简介

本实验基于 **ML-KEM-512（Kyber）** 实现一种后量子混合加密流程，用于验证 **密钥封装机制（KEM）+ 对称加密 + 数字签名（DSA）** 在文本数据场景下的可行性与正确性。

实验将密钥生成、数据加密和数据解密过程进行模块化拆分，便于多轮测试与复现实验结果。

## 2. 文件结构说明

```
.
├── keygen.py                 # 密钥生成与封装
├── encrypt.py                # 数据加密
├── decrypt.py                # 数据解密
│
├── public_key.txt             # 数据加密公钥
├── secret_key.txt             # 数据解密私钥
├── pk.txt            		   # 数字签名公钥
├── sk.txt                     # 数字签名私钥
├── signature.txt               # 数字签名
├── kem_ciphertext.txt         # KEM 封装密文（hex 编码）
├── shared_secret.txt          # KEM 共享密钥（hex 编码）
│
├── ciphertext_msg.txt         # 加密后的数据密文（hex 编码）
├── decrypted_message.txt      # 解密恢复的明文
│
├── 1.txt / 2.txt / ...        # 明文测试文件（UTF-8 文本）
└── README.md
```

## 3. 各脚本功能说明

### 3.1 `keygen.py` —— 密钥生成模块

- 功能：
  - 生成 ML-KEM-512 公钥与私钥
  - 基于公钥执行一次 KEM 封装
  - 生成共享密钥 `shared_secret`
- 输出文件：
  - `public_key.txt`
  - `secret_key.txt`
  - `pk.txt`
  - `sk.txt`
  - `kem_ciphertext.txt`
  - `shared_secret.txt`

📌 **说明**：
`keygen.py` **通常只需在实验开始时运行一次**，后续可重复使用生成的密钥材料进行多轮数据加解密测试。

### 3.2 `encrypt.py` —— 数据加密模块

- 功能：
  - 从指定文本文件中读取明文数据
  - 对明文数据进行签名
  - 使用已生成的 `shared_secret` 对数据进行对称加密
  - 输出加密后的数据密文
- 关键参数：

```python
message = load_text("xxx.txt")
```

其中 `xxx.txt` 为待加密的明文测试文件。

- 输出文件：
  - `ciphertext_msg.txt`
  - `signature.txt`

📌 **说明**：
每更换一次测试数据文件，仅需修改 `message = load_text("xxx.txt")` 并重新运行 `encrypt.py`。

### 3.3 `decrypt.py` —— 数据解密模块

- 功能：
  - 读取加密得到的 `ciphertext_msg.txt`
  - 使用相同的 `shared_secret` 执行对称解密
  - 恢复原始明文数据
  - 对签名进行验证确保消息的完整性
- 输出文件：
  - `decrypted_message.txt`

解密结果应与原始明文文件内容完全一致，用于验证加解密正确性。

## 4. 实验运行流程

### 方式一：推荐流程（密钥固定，多轮数据测试）

1. **首次运行密钥生成**

```bash
python keygen.py
```

1. **修改测试明文文件**

```python
message = load_text("1.txt")   # 或 2.txt、3.txt 等
```

1. **执行数据加密**

```bash
python encrypt.py
```

1. **执行数据解密**

```bash
python decrypt.py
```

1. **验证结果**

- 对比 `decrypted_message.txt` 与原始 `xxx.txt`

### 方式二：完整流程（每轮实验重新生成密钥）

在更换测试数据后，依次运行：

```bash
python keygen.py
python encrypt.py
python decrypt.py
```

该方式可用于验证系统在不同密钥条件下的稳定性。

