import numpy as np

# a. Chọn ma trận 3x3 khả nghịch
A = np.array([[2, 1, 1],
              [1, 3, 2],
              [1, 0, 0]])

# Kiểm tra định thức
det = np.linalg.det(A)
print(f"Determinant of A: {det}")

if det == 0:
    print("Ma trận không khả nghịch!")
else:
    print("Ma trận khả nghịch!")

# Tính ma trận nghịch đảo
A_inv = np.linalg.inv(A)

# b. Nhập họ tên hoặc mã số sinh viên
text = input("Nhập họ tên hoặc mã số sinh viên: ")

# c. Mã hóa
# Chuyển chuỗi thành mã ASCII
ascii_vals = [ord(c) for c in text]

# Thêm padding để chia hết cho 3
while len(ascii_vals) % 3 != 0:
    ascii_vals.append(0)

# Chia thành các vector 3 chiều
vectors = np.array(ascii_vals).reshape(-1, 3).T  # kích thước (3, n)

# Mã hóa: nhân ma trận A với các vector
encoded = np.dot(A, vectors)

print("\nMã hóa (ma trận kết quả):")
print(encoded)

# d. Giải mã
decoded = np.dot(A_inv, encoded)

# Làm tròn và chuyển về int
decoded = np.round(decoded).astype(int)

# Chuyển mã ASCII thành ký tự
decoded_chars = []
for col in decoded.T:
    for val in col:
        if val != 0:
            decoded_chars.append(chr(val))

decoded_text = "".join(decoded_chars)
print("\nGiải mã được:")
print(decoded_text)
