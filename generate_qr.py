"""
QR Code Generator for your Media Gallery

Usage:
    1. Install dependency:  pip install qrcode[pil]
    2. Run:                 python generate_qr.py YOUR_GITHUB_PAGES_URL

Example:
    python generate_qr.py https://YOURUSERNAME.github.io/my-gallery/

This generates a 'qr_code.png' file in the same directory.
"""

import sys
import qrcode

def generate(url: str):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_code.png")
    print(f"QR code saved to qr_code.png")
    print(f"Points to: {url}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_qr.py <YOUR_URL>")
        print("Example: python generate_qr.py https://username.github.io/my-gallery/")
        sys.exit(1)
    generate(sys.argv[1])
