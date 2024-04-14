#requirement: pip install captcha
#             pip install pillow
#             sudo apt-get install eog
#import captcha
from captcha.image import ImageCaptcha
from PIL import Image
import random
#function that generates a captcha to check if the user is a human or a bot
def generate_captcha():
    imagine = ImageCaptcha(width = 280, height = 90)
    #generate a random string of 6 characters
    random_str = ''.join([random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(6)])
    #generate the image of the captcha
    data = imagine.generate(random_str)
    #save the image of the captcha
    imagine.write(random_str, 'captcha.png')
    #open the image
    image = Image.open('captcha.png')
    image.show()
    print(f"The capcha answer is: {random_str}")
    #get user input
    user_input = input('Enter the string: ')
    return True if user_input == random_str else False

#Test the function
if __name__ == '__main__':
    print(generate_captcha())