'''Implement python script that calculate visible color of star based on its
temperature. The colors can be blue, white, yellow, orange and red.
Input of the script should be dictionary where key is name of the star
and value is a temperature. Output of the script should be colors
separated by newlines that has at least one star in it spectrum and star
names separated by comma. Script should has at least two functions:
one for calculating values and one for printing it.'''

STAR = {}
Name = None
Temperature = None
Color = None 

def calculating(Temperature):
    global Color
    if Temperature < 1500:
        Color = "blue"
    elif Temperature < 3000:
        Color = "white"
    elif Temperature < 4500:
        Color = "yellow"
    elif Temperature < 6000:
        Color = "orange" 
    elif Temperature < 8000:
        Color = "red"
    else: Color = "Color non-defigned"
    return Color

def printing(Color, Name):
    if (Color, Name != None):
       return print(f"{Color}, {Name}\n")

N = int((input("Input number of stars:")))

for i in range(N):
    Name = input("Input name of star:")
    Temperature = int(input("Input temperature of star:"))
    calculating(Temperature)
    STAR[Name] = Temperature
    printing(Color, Name)
