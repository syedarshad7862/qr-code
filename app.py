import streamlit as st
import qrcode
from PIL import Image
import io

st.set_page_config(page_title="QR Code Generator", layout="centered")

st.title("🔗 QR Code Generator")

url = st.text_input("Enter your URL:", placeholder="https://example.com")

if st.button("Generate QR Code") and url:
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    st.image(img, caption="Your QR Code", use_column_width=True)

    # Convert to bytes
    buf = io.BytesIO()
    img.save(buf)
    byte_im = buf.getvalue()

    st.download_button(
        label="📥 Download QR Code",
        data=byte_im,
        file_name="qr_code.png",
        mime="image/png"
    )
elif st.button("Generate QR Code") and not url:
    st.warning("Please enter a valid URL!")
