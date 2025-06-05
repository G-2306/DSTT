import numpy as np

def char_to_int(char):
    """Chuyển đổi ký tự thành số nguyên (A=1, B=2, ..., Z=26, khoảng trắng=0)."""
    if 'A' <= char <= 'Z':
        return ord(char) - ord('A') + 1
    elif 'a' <= char <= 'z':
        return ord(char) - ord('a') + 1
    elif char == ' ':
        return 0
    else:
        # Xử lý các ký tự không phải chữ cái hoặc khoảng trắng
        return 0 # Hoặc một giá trị khác tùy ý, ví dụ 27 cho ký tự đặc biệt

def int_to_char(num):
    """Chuyển đổi số nguyên thành ký tự (0=khoảng trắng, 1=A, ..., 26=Z)."""
    if num == 0:
        return ' '
    elif 1 <= num <= 26:
        return chr(num + ord('A') - 1)
    else:
        return '?' # Ký tự lỗi nếu số không nằm trong khoảng hợp lệ

def process_text(text):
    """Tiền xử lý văn bản: chuyển sang chữ hoa và chỉ giữ lại chữ cái, số và khoảng trắng."""
    processed_text = ""
    for char in text:
        if 'A' <= char <= 'Z' or 'a' <= char <= 'z' or char == ' ':
            processed_text += char.upper()
        # else:
            # Bỏ qua các ký tự không hợp lệ hoặc xử lý tùy theo yêu cầu
    return processed_text

# a. Tự chọn một ma trận khả nghịch 3x3 và chứng minh tính khả nghịch
# Ma trận A đã chọn:
A = np.array([
    [1, 2, 1],
    [0, 1, 2],
    [1, 0, 1]
])

print("Ma trận A đã chọn:")
print(A)

det_A = round(np.linalg.det(A)) # Làm tròn định thức để tránh sai số dấu phẩy động nhỏ
print(f"\nĐịnh thức của ma trận A: {det_A}")

if det_A != 0:
    print("Ma trận A khả nghịch (định thức khác 0).")
    A_inv = np.linalg.inv(A)
    print("\nMa trận nghịch đảo A_inv:")
    print(A_inv)
else:
    print("Ma trận A không khả nghịch. Vui lòng chọn ma trận khác.")
    exit()

# b. Nhập họ và tên hoặc mã số sinh viên
user_input = input("\nNhập họ và tên hoặc mã số sinh viên của bạn: ")
original_text = process_text(user_input)
print(f"Văn bản gốc đã xử lý: '{original_text}'")

# Chuyển đổi văn bản thành chuỗi số nguyên
text_numbers = [char_to_int(char) for char in original_text]

# Đảm bảo chiều dài của chuỗi số là bội số của 3
while len(text_numbers) % 3 != 0:
    text_numbers.append(0) # Thêm số 0 (khoảng trắng) vào cuối

print(f"Chuỗi số đã chuyển đổi (và bổ sung): {text_numbers}")

# c. Mã hóa họ và tên hoặc mã số sinh viên
encrypted_numbers = []
for i in range(0, len(text_numbers), 3):
    block = np.array(text_numbers[i:i+3]).reshape(3, 1) # Tạo vector cột
    encrypted_block = np.dot(A, block)
    # Lưu ý: Các giá trị mã hóa có thể không phải số nguyên nếu ma trận có số thực hoặc định thức lớn.
    # Trong trường hợp mã hóa đơn giản này, ta giữ nguyên giá trị thực.
    # Nếu muốn mã hóa thành số nguyên, cần một cơ chế modulo hoặc chuyển đổi khác.
    encrypted_numbers.extend(encrypted_block.flatten())

print(f"\nChuỗi số đã mã hóa (có thể là số thực): {encrypted_numbers}")

# d. Thực hiện giải mã với ma trận được chọn
decrypted_numbers = []
for i in range(0, len(encrypted_numbers), 3):
    block = np.array(encrypted_numbers[i:i+3]).reshape(3, 1) # Tạo vector cột
    decrypted_block = np.dot(A_inv, block)
    # Làm tròn để chuyển đổi lại thành số nguyên (vì kết quả giải mã cần là số nguyên)
    decrypted_numbers.extend(np.round(decrypted_block).flatten())

# Chuyển đổi chuỗi số đã giải mã thành văn bản
decrypted_text_list = [int_to_char(int(round(num))) for num in decrypted_numbers]
decrypted_text = "".join(decrypted_text_list).strip() # Loại bỏ khoảng trắng thừa cuối cùng

print(f"\nChuỗi số đã giải mã (làm tròn về nguyên): {decrypted_numbers}")
print(f"Văn bản đã giải mã: '{decrypted_text}'")

# Kiểm tra xem văn bản giải mã có khớp với văn bản gốc đã xử lý không
if decrypted_text == original_text:
    print("\nQuá trình mã hóa và giải mã thành công!")
else:
    print("\nCó lỗi trong quá trình mã hóa/giải mã hoặc dữ liệu không khớp chính xác.")
    print(f"Văn bản gốc đã xử lý: '{original_text}'")
    print(f"Văn bản giải mã: '{decrypted_text}'")