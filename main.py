# CMPT 120 Final Project
# Group 181
# Authors: Xuan Zi Ying and Ella McReynolds
# 06/08/2021
# Pixel art generator with 5 options

import image_helpers as ih
looping = True
cost = 0 
num_of_pixels_basic = 0

def convertHex(data):
  #from form (#aaaaaa)
  threedigitlist = [data[1:3], data[3:5], data[5:7]]
  converttoRGB = [int(threedigitlist[0],16), int(threedigitlist[1],16), int(threedigitlist[2],16)]
  return converttoRGB

def createPoster(file):
  img=[]
  x=0
  #create img
  for line in file:
    img.append([])
    linelist=line.strip("\n").strip("").split(",")
    width=len(linelist)
    for y in range(width):
      img[x].append([])
      data = linelist[y]
      pixels = convertHex(data)
      #print(pixels)
      img[x][y].append(pixels[0])
      img[x][y].append(pixels[1])
      img[x][y].append(pixels[2])
    x+=1
  #rotating img:
  wide=len(img)
  height=len(img[1])
  newimg=img[:]
  for i in range (len(newimg)):
      newimg[i]=newimg[i][:]
  for i in range(wide):
    for j in range(height):
      newimg[i][j]=img[j-1][i-1]
      newimg=newimg[0:height][0:width] 
  return newimg

def grayscale(img):
  #from csv file that is an img
  width = len(img)
  height = len(img[0])
  for x in range(width):
    for y in range(height):
      pixel = img[x][y]
      r = pixel[0]
      g = pixel[1]
      b = pixel[2]
      av = (r+g+b)/3
      pixel[0]=av
      pixel[1]=av
      pixel[2]=av
  return img 

def redBarsNarrow(img):
  #from csv file that is an img
  width = len(img)
  height = len(img[1])
  for x in range(width):
    for y in range(height):
      pixel = img[x][y]
      for n in range((width+30)//30):
        if x in range(0+30*n,16+30*n):
          r = pixel[0]
          g = pixel[1]
          b = pixel[2]
          if r >= 155:
            r = 255
          elif r < 155:
            r += 100
          if g <= 100:
            g = 0
          elif g > 100:
            g -= 100
          if b <= 100:
            b = 0
          elif b >100:
            b -=100
          pixel[0]=r
          pixel[1]=g
          pixel[2]=b
  return img

def redBarsWide(img):
  #from csv file that is an img
  width = len(img)
  height =len(img[1])
  for x in range(width):
    for y in range(height):
      pixel = img[x][y]
      for n in range((width+150)//150):
        if x in range(0+150*n,76+150*n):
          r = pixel[0]
          g = pixel[1]
          b = pixel[2]
          if r >= 155:
            r = 255
          elif r < 155:
            r += 100
          if g <= 100:
            g = 0
          elif g > 100:
            g -= 100
          if b <= 100:
            b = 0
          elif b >100:
            b -=100
          pixel[0]=r
          pixel[1]=g
          pixel[2]=b
  return img

def printoptions():
  print()
  print("Please choose from the following options,"
    "\n0 - Exit"
    "\n1 - Convert Hex color to RGB list"
    "\n2 - Create a Basic Poster"
    "\n3 - Create a Pixel Art Poster"
    "\n4 - Create a Greyscale Pixel Art Poster"
    "\n5 - Create a Pixel Art Poster with shades of red bars effect")
  print()
    # fix the lines later so it doesn't go out of border 

# 0 
def exitfunc():
  lowername = name.lower()
  # print ("lower name --> " , lowername) # test
  namelen = len(lowername)
  # print ("name length --> ", namelen) # test  
  totalascii = 0 
  letter_pos = 0
  for letter in lowername:
    # print(letter, letter_pos)# test
    if letter in ['a','e','i','o','u']:
      asciinumber = ord(letter)
      totalascii += asciinumber * letter_pos
      # print ("totalascii --> ", totalascii) #test
    letter_pos += 1
  luckynum = (totalascii + cost) % namelen
  # print("luckynum --> ", luckynum) # test
  print("You have entered 0, the tool now ends, here is your lucky number: ", int(luckynum))
  print("Your total cost is $", float(cost))

# function for 1
def isvalidhex(hexentry): #1
  if len(hexentry) != 7:
    return False
  if hexentry[0] != "#":
    return False
  for c in hexentry[1:7]:
    # i.lower() not in ['a','b','c','d','e','f'] and not i.isdigit()
    if not (c.lower() in ['a','b','c','d','e','f'] or c.isdigit()):
      return False
  return True

# 1
def option_one(): 
  print("Functionality 1, please enter hashtag followed by a 6 digit hex coded colour. ")
  hexentry = input("Your entry --> ")
  looping = True
  while looping == True :
    if isvalidhex(hexentry): 
      threedigitlist = [hexentry[1:3], hexentry[3:5], hexentry[5:7]]
      converttoRGB = [int(threedigitlist[0],16), int(threedigitlist[1],16), int(threedigitlist[2],16)]
      print("Here is the RGB value for ", hexentry)
      print(converttoRGB)
      looping = False
    else:
      print("Sorry I did not understand that. Please enter a valid entry.")
      print("Please enter # followed by a 6 digit hex coded colour. ")
      hexentry = input ("Your entry --> ")

#2
def option_two():
  file2 = open("basic.csv")
  print("Functionality 2 ")
  for data in file2:
    hexValues = data.strip().split(",")
    #print(hexValues) # test
    RGBvalues = list(map(convertHex, hexValues))
    #for hexValue in hexValues:
    #  RGB = convertHex(hexValue)
    #  RGBvalues.append(RGB) 
    width = len(RGBvalues) #200 rgbValue counted
    #print ("the list ", RGBvalues) # test 
    #print ("number of rgbValue " , width) # test 
  allpixels = []

  for rgbValue in RGBvalues:  
    column = [rgbValue] * width # each * 200
    allpixels.append(column)
  # print (allpixels[0])
  ih.saveImage(allpixels, 'poster-basic.jpg')
  print("The name of your poster is poster-basic.jpg")


def option_3():

  artlist=["cactus","flamingo","giraffe","house","parrot","tree"]
  sizelist=["50","100","200","400","800"]
  #ask user inputs

  print("Please choose the pixel art that you want to make a poster of:"
  "\n-",artlist[0],
  "\n-",artlist[1],
  "\n-",artlist[2],
  "\n-",artlist[3],
  "\n-",artlist[4],
  "\n-",artlist[5])
  print("\nTo select, type the art name (upper or lower case is ok)")
  art=input("====>").lower()
  if art in artlist:
    #choose size
    print("Please choose the size of your",art, "poster(in pixels):" 
    "\n-",sizelist[0],
    "\n-",sizelist[1],
    "\n-",sizelist[2],
    "\n-",sizelist[3],
    "\n-",sizelist[4],)
    print("To select, type the exact number provided. The poster will be a square.")
    size=input("====>")
    if size in sizelist:    
      #create file name
      filename= (art + "-" + size + ".csv")
    else:
      print("The size you indicated is not available. Try another option")
      filename = "invalid"

  #end loop if not
  else:
    print("The art you indicated is not available. Try another option.")
    filename = "invalid"

  return filename

#ask for picture and size -> save image
#return cost


#grayscale mostly same as option 3
#return cost
def option_4():
  #get file
  filename=option_3()
  if filename == "invalid":
    addicost = 4000

  else:  
    file = open(filename)
    img=createPoster(file)
    #apply grayscale
    grey=grayscale(img)
    #name and save
    filelist=filename.rstrip(".csv").split("-")
    print("The name of your poster is poster-grey-{}-{}.jpg".format(filelist[0],filelist[1]))
    ih.saveImage(grey, "poster-grey-{}-{}.jpg".format(filelist[0],filelist[1]))
    #calculate cost
    addicost = 0
    file = open(filename).readlines()
    for i in file:
      addicost+=1
    if addicost==50:
      addicost = 0
    else:
      addicost=(addicost/100)
  return addicost


def option_5():
  
  addicost = 0
  #get image/file
  filename = option_3()
  if filename == "invalid":
    addicost=4000
  else:
    file = open(filename)
    img=createPoster(file)
    filelist = filename.rstrip(".csv").split("-")
    #now choose bars
    print("Please specify the type of bar effect you want. If I do not understand I'll assume wide):"
    "\n- narrow"
    "\n- wide")
    barchoice = input("\n===>").lower()
    #different functions name/save for each
    if barchoice == "narrow":
      red=redBarsNarrow(img)
      print("The name of your poster is poster-bars-15-{}-{}.jpg".format(filelist[0],filelist[1]))
      ih.saveImage(red, "poster-bars-15-{}-{}.jpg".format(filelist[0],filelist[1]))
  #wide
    else:
      red=redBarsWide(img)
      print("The name of your poster is poster-bars-75-{}-{}.jpg".format(filelist[0],filelist[1]))
      ih.saveImage(red, "poster-bars-75-{}-{}.jpg".format(filelist[0],filelist[1]))
  #calculate cost
    file = open(filename).readlines()
    for i in file:
      addicost+=1
    if addicost==50:
      addicost = 0
    else:
      addicost=(addicost/50)

  return addicost


#starting the actual program here

print("Welcome to the pixel image creator tool!") 
print()
name = input ("What is your name? --> ")
print("\nNice to meet you,", name)
print()
print("Please choose options to generate art. You may repeat options. "
"\n\nThe tool will save your art as jpg files in this folder."
"\n\nWhen you exit the tool you will be provided the cost, and also a lucky number!")
# fix the lines later so it doesn't go out of border 

printoptions()

option = int(input ("Your option --> "))

while option != 0: 
  if option == 1: # functionality 1 convert hex to rgb
    print("Functionality 1. Convert Hex color to RGB list")
    option_one()
    cost += 0.25
    print("This will cost you $0.25")
    print("New total cost is: $", float(cost))
    printoptions()
    option = int(input ("Your new option --> "))
    
  elif option == 2:
    print("Functionality 2. Create a Basic Poster")
    option_two()
    cost += 1
    print("This will cost you: $1")
    print("New total cost is: $", float(cost))
    printoptions()
    option = int(input ("Your new option --> "))

  elif option == 3:
    addicost = 0
    print("Functionality 3. Create a Pixel Art Poster")
    #open/get file
    filename = option_3()
    if filename == "invalid":
      printoptions()
      option = int(input ("Your new option --> "))
    else:
      file = open(filename)
      img=createPoster(file)
      #name and save file
      filelist=filename.rstrip(".csv").split("-")
      print("The name of your poster is poster-original-{}-{}.jpg".format(filelist[0],filelist[1]))
      ih.saveImage(img, "poster-original-{}-{}.jpg".format(filelist[0],filelist[1]))
      #calculate cost
      file = open(filename).readlines()
      for i in file:
        addicost+=1
      if addicost==50:
        addicost = 0
        cost=cost
      else:
        addicost=(addicost/100)
        cost+=(addicost)
      print("This will cost you: $", addicost)
      print("New total cost is: $", cost)
      #restart loop
      printoptions()
      option = int(input ("Your new option --> "))

  elif option == 4:
    print("Functionality 4. Create a Grayscale Pixel Art Poster ")
    #get grey image and calculate cost
    greycost=option_4()
    if greycost==4000:
      printoptions()
      option = int(input ("Your new option --> "))
    else:
      cost += greycost
      print("This will cost you: $", greycost)
      print("New total cost is: $", float(cost))
      printoptions()
      option = int(input ("Your new option --> "))

  elif option == 5:
    print("Functionality 5. Create a Pixel Art Poster With Red Bars")
    redcost = option_5()
    if redcost==4000:
      printoptions()
      option = int(input ("Your new option --> "))
    else:
      cost += redcost
      print("This will cost you $", redcost)
      print("New total cost is: $", float(cost))
      printoptions()
      option = int(input ("Your new option --> "))

  #bonus
  #elif option == 6:
   # print("Functionality 6")

  else: 
    print ("Sorry I don't understand, please enter a valid value.")
    option = int(input ("Your option --> "))
  

exitfunc()

