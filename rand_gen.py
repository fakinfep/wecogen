import random
import time
import read_wordlist

def GenerateRandomTitle():
    # Generate a random title
    # Return: string
    length = random.randint(3, 10)
    random.seed(time.time())
    # Choose a random letter from the alphabet
    title = [chr(random.randint(97, 122)) for i in range(length)]
    # How many letters are going to be capitalized
    num_capitalized = random.randint(1, length-random.randint(1, 2))
    # Capitalize Letters
    for i in range(num_capitalized):
        title[random.randint(0, length-1)] = title[random.randint(0, length-1)].upper()
    # Join the list into a string
    title = ''.join(title)
    return title

def GenerateRandomRGBAColor():
    # Generate a random color
    # Return: string
    random.seed(time.time())
    color_rgba = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color_rgba

def GenerateRandomPicture():
    # Generate a random picture
    # Return: string
    random.seed(time.time())
    # Choose a random picture with randomly size , content , grayscale and blur from picsum
    picture = 'https://picsum.photos/'+str(random.randint(200,1080))+'/'+str(random.randint(300,1920))+'/?image=' + str(random.randint(0, random.randint(1, 1084)))
    if random.randint(0, 1) == 1:
        picture += '&grayscale'
    elif random.randint(0, 1) == 1:
        picture += '&blur'
    elif random.randint(0, 1) == 1:
        picture += '&blur='+str(random.randint(1,2))+'&grayscale'
    return picture

def GenerateRandomSizeFixedPicture(length,width):
    # Generate a random picture with fixed size
    # Return: string
    random.seed(time.time())
    # Choose a random picture with randomly content , grayscale and blur from picsum
    picture = 'https://picsum.photos/'+str(length)+'/'+str(width)+'/?image=' + str(random.randint(0, random.randint(1, 1084)))
    if random.randint(0, 1) == 1:
        picture += '&grayscale'
    elif random.randint(0, 1) == 1:
        picture += '&blur'
    elif random.randint(0, 1) == 1:
        picture += '&blur='+str(random.randint(1,2))+'&grayscale'
    return picture

def GenerateRandomText(filename):
    # Generate a random text
    # Return: string
    random.seed(time.time())
    # Choose a random text from the wordlist
    length = random.randint(1, 1000)
    text = ''
    for i in range(length):
        text += read_wordlist.read_wordlist(filename)[random.randint(0, len(read_wordlist.read_wordlist(filename))-1)]
        if random.randint(0, 1) == 1:
            text += ' '
        elif random.randint(0, 1) == 1:
            text += '. '
        elif random.randint(0, 1) == 1:
            text += ', '
        elif random.randint(0, 1) == 1:
            text += '! '
        elif random.randint(0, 1) == 1:
            text += '? '
        elif random.randint(0, 1) == 1:
            text += '; '
        elif random.randint(0, 1) == 1:
            text += ': '
        elif random.randint(0, 1) == 1:
            text += '- '
        elif random.randint(0, 1) == 1:
            text += '_ '
        elif random.randint(0, 1) == 1:
            text += '/ '
        elif random.randint(0, 1) == 1:
            text += '\\ '
        elif random.randint(0, 1) == 1:
            text += '| '
        if random.randint(0, 1) == 1:
            text += ' \n '
    return text