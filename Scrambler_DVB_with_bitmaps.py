import random
# from bitmap import BitMap
from PIL import Image
sync = []
scrambler_output = []
descrambler_output = []
first_sync = []
size_of_bitmap = 50
# Definicja sumy XOR


def xor(a, b):
    if int(a) - int(b) == 0:
        return 0
    else:
        return 1


# Tworzenie sync/poczatkowe 15 pseudolosowych bitow w scramblerze
def fill_sync(tab, tab2):
    for i in range(size_of_bitmap*size_of_bitmap):
        tab.append(random.randint(0, 1))
        tab2.append(tab[i])
    return tab


# wypełnienie scramblera i wypisanie poczatkowych liczb pseudolosowych
fill_sync(sync, first_sync)
informal_sync = [str(i) for i in sync]
# print('\nCiag losowy SYNC: ' + ''.join(informal_sync))

# Pobranie słowa z pliku
raw_binary = [random.randint(0, 1) for i in range(size_of_bitmap*size_of_bitmap)]
# print("Przed scramblingiem: " + str(raw_binary))


# funkcja scramblujaca
def scrambling(tab):
    for i in range(len(tab)):
        temp = len(sync)
        scrambler_output.append(xor(xor(sync[13], sync[14]), tab[i]))
        while temp > 1:
            sync[temp-1] = sync[temp-2]
            temp -= 1
        sync[0] = xor(sync[13], sync[14])
    return scrambler_output


# funkcja descramblujaca
def descrambling(tab):
    for i in range(len(tab)):
        temp = len(first_sync)
        descrambler_output.append(xor(xor(first_sync[13], first_sync[14]), tab[i]))
        while temp > 1:
            first_sync[temp-1] = first_sync[temp-2]
            temp -= 1
        first_sync[0] = xor(first_sync[13], first_sync[14])
    return descrambler_output

# wykonanie scramblingu i wpisanie efektow
scramblud = scrambling(raw_binary)
informal_scrambled = [str(i) for i in scrambler_output]
# print('Po scramblingu: ' + ''.join(informal_scrambled))


# wykonanie descramblingu i wpisanie efektow
# descrambling(scrambler_output)
descrambled = descrambling(scramblud)
informal_descrambled = [str(i) for i in descrambled]
# print('Po descramblingu: ' + ''.join(informal_descrambled))

# wypelnienie obrazka sygnalem wejsciowym przed scramblingiem
img1 = Image.new('1', (size_of_bitmap, size_of_bitmap))  
pixels1 = img1.load()  # Create the pixel map
img2 = Image.new('1', (size_of_bitmap, size_of_bitmap)) 
pixels2 = img2.load()
img3 = Image.new('1', (size_of_bitmap, size_of_bitmap))
pixels3 = img3.load()
# img.show()
for i in range(img1.size[0]):    # For every pixel:
    for j in range(img1.size[1]):
        pixels1[i, j] = raw_binary[size_of_bitmap*i + j]
        pixels2[i, j] = scramblud[size_of_bitmap*i + j]
        pixels3[i, j] = descrambled[size_of_bitmap*i + j]

img1.show(title='Przed  scramblingiem')
img2.show(title='Po scramblingu')
img3.show(title='Po rescramblingu')
