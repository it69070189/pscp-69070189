"""Colors"""
def main():
    """colors"""

    color1 = input().capitalize()
    color2 = input().capitalize()

    color = {color1, color2}
    if color == {"Red", "Yellow"}:
        print("Orange")
    elif color == {"Red", "Blue"}:
        print("Violet")
    elif color == {"Yellow", "Blue"}:
        print("Green")
    elif color == {"Red"}:
        print("Red")
    elif color == {"Yellow"}:
        print("Yellow")
    elif color == {"Blue"}:
        print("Blue")
    else:
        print("Error")

main()
