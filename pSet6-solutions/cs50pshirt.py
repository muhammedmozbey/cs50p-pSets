'''from PIL import Image
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few CLA")
    elif len(sys.argv) > 3:
        sys.exit("Too many CLA")

    try:
        if sys.argv[1].endswith(".jpeg"):
            if sys.argv[2].endswith(".jpeg"):
                pass
            else:
                sys.exit("Input and Output have different extensions")
        elif sys.argv[1].endswith(".png"):
            if sys.argv[2].endswith(".png"):
                pass
            else:
                sys.exit("Input and Output have different extensions")

        try:
            if sys.argv[1] == "before1.jpg":
                with Image.open("before1.jpg") as bfrimg1: #all good
                    shirt = Image.open("shirt.png")
                    resized = resize_shirt(shirt, (1000, 1000))
                    bfrimg1.paste(resized, (110, 360), resized)
                    bfrimg1.save(sys.argv[2])
            elif sys.argv[1] == "before2.jpg":
                with Image.open("before2.jpg") as bfrimg2:
                    shirt = Image.open("shirt.png")
                    resized = resize_shirt(shirt, (1300, 1750))
                    bfrimg2.paste(resized, (-40, -200), resized)
                    bfrimg2.save(sys.argv[2])
            elif sys.argv[1] == "before3.jpg":
                with Image.open("before3.jpg") as bfrimg3:
                    shirt = Image.open("shirt.png")
                    resized = resize_shirt(shirt, (1000, 1400))
                    bfrimg3.paste(resized, (110, 50), resized)
                    bfrimg3.save(sys.argv[2])


        except Exception as e:
            sys.exit(f"Error occured: {e}")

    except Exception as e:
        sys.exit(f"Error occured: {e}")


def resize_shirt(shirt_image, new_size):
    return shirt_image.resize(new_size, Image.Resampling.LANCZOS)

if __name__ == "__main__":
    main() '''


from PIL import Image
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few CLA")
    elif len(sys.argv) > 3:
        sys.exit("Too many CLA")


    try:
        if not (sys.argv[1].endswith(".jpg") or sys.argv[1].endswith(".png")) or not (sys.argv[2].endswith(".jpg") or sys.argv[2].endswith(".png")):
            sys.exit("Invalid input")
        else:
            if sys.argv[1].endswith(".jpg") == sys.argv[2].endswith(".jpg"):
                pass
            else:
                sys.exit("Input and Output have different extensions")
            if sys.argv[1].endswith(".png") == sys.argv[2].endswith(".png"):
                pass
            else:
                sys.exit("Input and Output have different extensions")

        try:
            if sys.argv[1] == "before1.jpg":
                with Image.open("before1.jpg") as bfrimg1: #all good
                    shirt = Image.open("shirt.png")
                    resized = resize_shirt(shirt, (1000, 1000))
                    bfrimg1.paste(resized, (110, 360), resized)
                    bfrimg1.save(sys.argv[2])
            elif sys.argv[1] == "before2.jpg":
                with Image.open("before2.jpg") as bfrimg2:
                    shirt = Image.open("shirt.png")
                    resized = resize_shirt(shirt, (1300, 1750))
                    bfrimg2.paste(resized, (-40, -200), resized)
                    bfrimg2.save(sys.argv[2])
            elif sys.argv[1] == "before3.jpg":
                with Image.open("before3.jpg") as bfrimg3:
                    shirt = Image.open("shirt.png")
                    resized = resize_shirt(shirt, (1000, 1400))
                    bfrimg3.paste(resized, (110, 50), resized)
                    bfrimg3.save(sys.argv[2])
            else:
                sys.exit(f"File does not exist: {sys.argv[1]}")

        except Exception as e:
            sys.exit(f"Error occured: {e}")

    except Exception as e:
        sys.exit(f"Error occured: {e}")


def resize_shirt(shirt_image, new_size):
    return shirt_image.resize(new_size, Image.Resampling.LANCZOS)

if __name__ == "__main__":
    main()
