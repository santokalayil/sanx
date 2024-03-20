from PIL import Image

from sanx.paths import LOGO_PATH

logo_img = Image.open(LOGO_PATH)


# company logo
logo_style = {
    "position": "absolute",
    "top": "10px",
    "left": "10px",
    "height": "100px",  # Adjust the height as needed
    "width": "auto",  # Keep the width proportional
}
