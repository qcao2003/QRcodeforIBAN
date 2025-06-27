import qrcode

# 🔑 你的私钥（用你的私钥替换下面这行）
private_key = "c0ffee1234567890c0ffee1234567890c0ffee1234567890c0ffee1234567890"

# 生成二维码
qr = qrcode.QRCode(
    version=1,  # 自动选合适的大小
    error_correction=qrcode.constants.ERROR_CORRECT_M,  # 容错率
    box_size=10,
    border=4,
)
qr.add_data(private_key)
qr.make(fit=True)

# 渲染成图片
img = qr.make_image(fill_color="black", back_color="white")

# 保存到文件
img.save("private_key_qr.png")
img.show("private_key_qr.png")
print("✅ 已生成二维码，文件名：private_key_qr.png")

