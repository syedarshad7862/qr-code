import streamlit as st
import qrcode
from PIL import Image
import io

st.set_page_config(page_title="QR Code Generator", layout="centered")

st.title("🔗 QR Code Generator")

url = st.text_input("Enter your URL:", placeholder="https://example.com")

if st.button("Generate QR Code", key="generate_qr"):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    # Display image
    st.image(img, caption="Your QR Code", use_container_width=True)

    # Convert to bytes
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    # Download button
    st.download_button(
        label="📥 Download QR Code",
        data=byte_im,
        file_name="qr_code.png",
        mime="image/png",
        key="download_qr"
    )
else:
    st.warning("⚠️ Please enter a valid URL!")
