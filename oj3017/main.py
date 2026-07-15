"""bill"""
def main():
    """bill"""
    price = int(input())
    service = (price * 10) / 100
    vat = 107 / 100
    if service < 50:
        service = 50
    elif service > 1000:
        service = 1000
    print(f"{(price + service) * vat:.2f}")
main()
