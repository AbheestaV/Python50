import sys

from PIL import Image, ImageOps

def main():
    formats = ["jpg", "jpeg", "png"]
    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 3:
        print("Too less command-line arguments")
        sys.exit(1)

    elif not sys.argv[1].endswith("jpg") and not sys.argv[1].endswith("jpeg") and not sys.argv[1].endswith("png"):
        print("Invalid input")
        sys.exit(1)

    _,format1 = sys.argv[1].split(".")
    _,format2 = sys.argv[2].split(".")
    if format1 != format2:
        print("Input and output have different extensions")
        sys.exit(1)
    shirt(sys.argv[1], sys.argv[2])

def shirt(a, b):
    image = Image.open(a)
    shirt = Image.open("shirt.png")
    image2 = ImageOps.fit(image, shirt.size, method = 0, bleed = 0.0, centering =(0.5, 0.5))
    image2.paste(shirt, box = None, mask = shirt)
    image2.save(b)




if __name__ == "__main__":
    main()