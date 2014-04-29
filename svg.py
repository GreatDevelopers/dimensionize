class SVG():
    # Opening the SVG file
    def __init__(self, filename, height, width):
        self._file = open(filename, "w+")
        self._file.write('<svg height="' + str(height) + '" width="'
        + str(width) + '">\n')

    # Just supports the circle rightnow.
    def circle(self, cx, cy, radius):

        # The circle itself is drawn!
        self._file.write( '\t<circle cx="' + str(cx) + '" cy="' + str(cy)
         + '" r="' + str(radius) 
         + '" stroke="black" stroke-width="1" fill="white" />\n')

        # The lines for dimension
        self._file.write('\t<line x1="' + str(cx) + '" y1="' + str(cy)
         + '" x2="' + str(cx-radius) + '" y2="' + str(cy-radius)
         + '" style="stroke:rgb(0,0,0);stroke-width:1" />\n')
        
        self._file.write('\t<line x1="' + str(cx-radius) + '" y1="'
         + str(cy-radius) + '" x2="' + str(cx-radius-(radius/10))
         + '" y2="' + str(cy-radius) 
         + '" style="stroke:rgb(0,0,0);stroke-width:1" />\n')

        # Dimensioning Text
        self._file.write('\t<text x="' + str(cx-radius-(radius/10))
         + '" y="' + str(cy-radius-(radius/10)) + '" fill="black"> R '
         + str(radius) + '</text>\n')

    # Closing the SVG File
    def savefile(self):
        self._file.write('</svg>\n')
        self._file.close()

# Open the file
_filepath = raw_input("Enter absoulte path of file\n \
 For Example : /home/user/abc.svg : ")

# Create a new object to create the file
a = SVG(_filepath, 1000, 1000)

# Create new circles CenterX, CenterY, Radius
a.circle(300, 300, 100)
a.circle(500, 300, 40)
a.circle(300, 200, 50)
a.circle(300, 900, 57)

# Bye bye!
a.savefile()
