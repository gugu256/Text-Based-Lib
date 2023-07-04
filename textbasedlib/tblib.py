#                          ------------------                              #
#                          | Text-Based Lib |                              #
#                          ------------------                              #
#                                                                          #
# Devs : @NaolNinja, @gugu256, @canard, @El1teWatermelon                   #
# Originally created my gugu256 (aka PancakeDev) www.gugu256.github.io     #
# With the help of canard (aka devplodocus) www.canard101.github.io        #
# Typewriting effect by NaolNinja (www.replit.com/@NaolNinja)              #
# PCI File system by El1teWatermelon (www.github.com/El1teWatermelonGames) #

import platform # To detect the os type
import sys # Used in the typewrite function
import time # To sleep, obviously
import pickle # To save and get the data 
import colorama # To color the console
from os import system as cmd
from os import getcwd, listdir
import os

cmd("") # Init command prompt
colorama.init() # Initializes colorama

__version__ = "1.2"

# DATA #

arg_ = ""

try:
  arg_ = sys.argv[1]
  if arg_ == "new_project":
    os.mkdir(sys.argv[2])
    os.chdir(sys.argv[2])
    ostype = platform.system()
    cmd('echo ' + "import textbasedlib.tblib as tblib\nprint(dialogs[0])" + " > main.py")
    cmd('echo ' + "Our adventure is set in the fair town of Reinsburg.. " + '> dialogs.txt')
    print(f"{sys.argv[2]} Project created !")
    input("Press enter to continue./")
except:
  pass

files = listdir(getcwd())
if "dialogs.txt" in files:
  dialogspath = "dialogs.txt" # Opens the default file for dialogs
  dialogs = open(dialogspath, "r").read() # Reads it
  dialogs = dialogs.splitlines() # Makes the lines of the dialogs file a list
else:
  dialogspath = ""
  dialogs = []

colors = { 
  """
  Quicker way to add color in the console"""
  "red": colorama.Fore.RED,
  "green": colorama.Fore.GREEN,
  "yellow": colorama.Fore.YELLOW,
  "blue": colorama.Fore.BLUE,
  "default": colorama.Style.RESET_ALL,
}

style = { 
  """
  Quicker way to add style in the console"""
  "dim": colorama.Style.DIM,
  "normal": colorama.Style.NORMAL,
  "bright": colorama.Style.BRIGHT
}
 
# Color codes for the PCI system
CEND = "\u001b[0m"
CBLACK = "\u001b[40m"
CRED = "\u001b[41m"
CGREEN = "\u001b[42m" 
CYELLOW = "\u001b[43m"
CBLUE = "\u001b[44m"
CMAGENTA = "\u001b[45m"
CCYAN = "\u001b[46m"
CWHITE = "\u001b[47m"
CBBLACK = "\u001b[40;1m"
CBRED = "\u001b[41;1m"
CBGREEN = "\u001b[42;1m"
CBYELLOW = "\u001b[43;1m"
CBBLUE = "\u001b[44;1m"
CBMAGENTA = "\u001b[45;1m"
CBCYAN = "\u001b[46;1m"
CBWHITE = "\u001b[47;1m"

save_sentence = "Saved data successfully!" # Sentence to say when data is saved
# You can change it if you need it in another language

# PIXEL CONSOLE IMAGE SYSTEM
# More info on https://github.com/El1teWatermelonGames/Pixel-Console-Image-Viewer
# The Pixel-Console-Image uses a hexadecimal color system (16 colors to pick from)
# 0 | BLACK
# 1 | RED
# 2 | GREEN
# 3 | YELLOW
# 4 | BLUE
# 5 | MAGENTA
# 6 | CYAN
# 7 | WHITE
# 8 | BRIGHT BLACK
# 9 | BRIGHT RED
# A | BRIGHT GREEN
# B | BRIGHT YELLOW
# C | BRIGHT BLUE
# D | BRIGHT MAGENTA
# E | BRIGHT CYAN
# F | BRIGHT WHITE

# Data and essential functions for Pixel-Console-Image
def processLines(image): # A function needed in pci (odn't worry about it)
  image = open(image, 'r') # Open the image file
  data = []
  for line in image:
    data.append(line.replace("\n", "")) # Remove \n character from start of line and add the line to the list
  image.close()
  return data
def processPixel(data, patfile): # A function needed in pci (odn't worry about it)
  out = []
  for line in data: # Cycle through each line of data
    newLine = ""
    for char in line: # Cycle through character
      if patfile == False: char = char.replace(char, appendPixel(char, "  ")) # Normal image processing
      if patfile == True: char = char.replace(char, appendPixel(char, char+" ")) # Pat file processing
      newLine += char
    out.append(newLine)
  return out
def appendPixel(char, outChar):
  out = ""
  if char == "0": out = CBLACK
  elif char == "1": out = CRED
  elif char == "2": out = CGREEN
  elif char == "3": out = CYELLOW
  elif char == "4": out = CBLUE
  elif char == "5": out = CMAGENTA
  elif char == "6": out = CCYAN
  elif char == "7": out = CWHITE
  elif char == "8": out = CBBLACK
  elif char == "9": out = CBRED
  elif char == "A": out = CBGREEN
  elif char == "B": out = CBYELLOW
  elif char == "C": out = CBBLUE
  elif char == "D": out = CBMAGENTA
  elif char == "E": out = CBCYAN
  elif char == "F": out = CBWHITE
  elif char == " ": out = CEND
  else:
    print(f"Invalid char in image file: {char}")
    exit(1)
  return str(out + outChar + CEND)
def getImage(imageData):
  for line in imageData:
    print(line)

# Now THIS is where it gets interesting !
def print_pixel_image(imgpath: str):
  """
  Example usage : print_pixel_image("splashscreen.pci")
  """
  getImage(processPixel(processLines(imgpath), False))

def print_pixel_set(pixelset: list):
  """
  Example usage : print_pixel_set(splashscreen)
  """
  getImage(processPixel(pixelset, False))



# OTHER FUNCTIONS #

def w(seconds): 
  """
  Equivalent of time.sleep(), but quicker to use
  """ 
  time.sleep(seconds)

def clear(): 
  """
  Cross-platform console clearer
  """
  ostype = platform.system()
  if ostype == "Linux" or ostype == "Darwin":
    cmd("clear")
  else:
    cmd("cls")

def q(): 
  """
  Basic quit function
  """
  c = inp("Are you sure you want to quit ?\ny/n")
  if c == "y":
    quit()
  else:
    pass

def inp(prompt: str): 
  """
  Quicker complete input
  """
  userchoice = input(f"{prompt}\n> ")
  return userchoice

def pe(): 
  """
  "Press enter" basic function
  """
  input("Press Enter to continue./")

def pev(verb): 
  """
  Press enter" basic function with the possibilty to change the verb
  Example : pev(mine) --> "Press enter to mine" 
  """
  input(f"Press Enter to {verb}./")

def tw(text: str): 
  """
  Typewrites text (by @NaolNinja on replit.com)
  """
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    w(0.065)
  print("")

def titlescreen(title: str, underline_char: str, creds: str): 
  """
  Simple way to output a title screen
  """
  print(title)
  print(len(title)*underline_char)
  print(creds)
  print("")

def set_dialogs(path: str): 
  """
  To get a different dialogs set if needed
  """
  global dialogspath
  global dialogs
  dialogspath = path
  try:
    dialogs = open(dialogspath, "r").read()
  except FileNotFoundError:
    raise FileNotFoundError("Dialogs file not found")
  dialogs = dialogs.splitlines()

def passage(text: str, options: list, functions: list, typewrite: bool): 
  """
  Passage function
  """
  while True:
    clear()
    if typewrite:
      tw(text)
    else:
      print(text)
    print("")
    for i in range(0, len(options)):
      print(f"{i+1} : {options[i]}")
    userchoice = input("> ")
    if int(userchoice) <= (len(options)+1):
      f = functions[(int(userchoice) - 1)]
      break
    elif userchoice == "q" or userchoice == "quit":
      q()
    else:
      print("Please enter a choice")
      pe()
  eval(f)

def say(text: str, typewrite: bool): 
  """
  Better way to print text
  """
  if typewrite:
    tw(text)
  else:
    print(text)
  pe()

def save_data(data: object, filename: str): 
  """
  Complete saving function
  """
  with open(filename, "wb") as pickle_file:
    pickle.dump(data, pickle_file)
  print(save_sentence)
  pe()
  
def load_data(filename: str): 
  """
  Returns data from a saved file"""
  with open(filename, "rb") as pickle_file:
    data = pickle.load(pickle_file)
  return data

# END #