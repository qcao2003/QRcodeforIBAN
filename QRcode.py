import qrcode


def generate_iban_qr(iban, amount, currency="EUR", name="", bic="", reference="", output_file="iban_qr_with_bic.png"):
    """
    生成包含 IBAN 和 SWIFT/BIC 的二维码，符合扩展 SEPA 规范。

    :param iban: 收款方的 IBAN 号码。
    :param amount: 支付金额（可选）。
    :param currency: 货币类型（默认为 EUR）。
    :param name: 收款方名称。
    :param bic: 收款方的 SWIFT/BIC 代码（可选）。
    :param reference: 支付参考（可选）。
    :param output_file: 输出二维码的文件路径。
    """
    # 构造扩展的 SEPA QR 格式字符串
    qr_data = (
        f"BCD\n"  # 服务标签，固定为 BCD
        f"001\n"  # 版本号
        f"1\n"  # 标准，1 = SEPA 规则
        f"SCT\n"  # 服务模式，SCT 表示单一信用转账
        f"{name}\n"
        f"{bic}\n"  # 添加 SWIFT/BIC
        f"{iban}\n"
        f"{currency}{amount:.2f}\n"
        f"{reference}\n"
    )

    # 生成二维码
    qr = qrcode.QRCode(
        version=1,  # 控制二维码大小，1 是最小
        error_correction=qrcode.constants.ERROR_CORRECT_M,  # 容错级别
        box_size=10,  # 每个方块的像素大小
        border=4,  # 边框大小
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    # 创建二维码图像并保存
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)
    img.show(output_file)
    print(f"二维码已保存至 {output_file}")


# 示例调用
iban = "BE55905357671844"  # 示例 IBAN
bic = "TRWIBEB1XXX"  # 示例 SWIFT/BIC 代码
amount = 10  # 支付金额
name = "Cui Zhen Wu"  # 收款方名称
reference = "from fiat24"  # 支付参考

generate_iban_qr(iban, amount, currency="EUR", name=name, bic=bic, reference=reference)
