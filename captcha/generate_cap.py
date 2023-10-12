from captcha.image import ImageCaptcha

def generate_captcha(code):
    image = ImageCaptcha()
    data = image.generate(code)
    image.write(code, 'captcha.png')

if __name__ == "__main__":
    code = "12345"  # Replace this code with your desired CAPTCHA code
    generate_captcha(code)
    print("CAPTCHA image generated. Check 'captcha.png' in the current directory.")

