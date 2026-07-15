"""pro"""
def main():
    """pro"""
    kon = int(input())
    pay = int(input())
    price = int(input())
    eat = int(input())

    group = eat // kon
    other = eat % kon
    print(((group * pay) + other) * price)
main()
