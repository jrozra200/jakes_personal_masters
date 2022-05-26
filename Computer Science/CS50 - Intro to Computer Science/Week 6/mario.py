def main():
    height = get_height()
    width = get_width()
    print_block(height, width)
    
def print_block(height, width):
    for i in range(height):
        print("#" * width)

def get_height():
    while True:
        try: 
            n = int(input("Height: "))
            if n > 0:
                return n
            else:
                print("Height must be greater than 0")
        except ValueError:
            print("Height must be an int")

def get_width():
    while True:
        try: 
            n = int(input("Width: "))
            if n > 0:
                return n
            else:
                print("Width must be greater than 0")
        except ValueError:
            print("Width must be an int")
    
if __name__ == "__main__":
    main()
