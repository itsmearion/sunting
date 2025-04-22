# utils/format_text.py

def generate_order_format(username: str) -> str:
    return (
        f"Salutations I'm @{username}, I’d like to place an order for catalog t.me/blakeshley listed at Blakeshley, "
        f"Using payment method [dana, gopay, qriss, spay, ovo, bank.] "
        f"The total comes to IDR [00.000] Inrush add 5k [yay/nay]. "
        f"Kindly process this, Thanks a bunch."
    )