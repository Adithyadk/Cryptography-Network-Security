def elliptic_curve_addition(x1, y1, x2, y2, a, p):
    if x1 == x2 and y1 == y2:
        # Point doubling
        if y1 == 0:
            # Point at infinity
            return float('inf'), float('inf')

        lambda_val = (3 * x1**2 + a) * pow(2 * y1, -1, p) % p
    else:
        # Point addition
        if x1 == x2:
            # Points have the same x-coordinate, i.e., P + P
            lambda_val = (3 * x1**2 + a) * pow(2 * y1, -1, p) % p
        else:
            # Points are distinct
            lambda_val = (y2 - y1) * pow(x2 - x1, -1, p) % p

    x3 = (lambda_val**2 - x1 - x2) % p
    y3 = (lambda_val * (x1 - x3) - y1) % p

    return x3, y3


def multiply(e1, d, a, p):
    b = [e1[0], e1[1]]
    for i in range(1, d):
        b = addition(e1, b, a, p)
    b[0] %= p
    b[1] %= p
    return b


def addition(p1, p2, a, p):
    c = [0, 0]  # Initialize c before the if-else block
    if p1[0] == p2[0] and p1[1] == p2[1]:
        k = (((3 * (p1[0] ** 2)) + a) * (modInverse((2 * p1[1]), p))) % p
    else:
        k = ((p2[1] - p1[1]) * (modInverse((p2[0] - p1[0]), p))) % p

    c[0] = (k ** 2 - p1[0] - p2[0]) % p
    c[1] = (k * (p1[0] - c[0]) - p1[1]) % p
    return c


def modInverse(x, n):
    if gcd(x, n) != 1:
        return -1
    return pow(x, -1, n)


def gcd(m, n):
    if n == 0:
        return m
    return gcd(n, m % n)


def main():
    p, a, b, d, r = 0, 0, 0, 0, 0
    e1 = [0, 0]
    e2 = [0, 0]
    P_Initial = [0, 0]
    C1 = [0, 0]
    C2 = [0, 0]
    P_Final = [0, 0]
    temp = [0, 0]
    tempI = [0, 0]

    print("Enter value of p (prime number): ")
    p = int(input())
    print("Enter the value of a: ")
    a = int(input())
    print("Enter the value of b: ")
    b = int(input())
    print("Enter e1 value (array of coordinates x and y, separated by space): ")
    e1_input = input().split()
    e1[0] = int(e1_input[0])
    e1[1] = int(e1_input[1])

    print("Enter d (private key) value: ")
    d = int(input())

    # Convert e1 to a list before calling multiply
    e2 = multiply(list(e1), d, a, p)
    if e2[0] < 0:
        e2[0] += p
    if e2[1] < 0:
        e2[1] += p

    print("(E, e1, e2) is:")
    print(f"(E{p},{a},{b})")
    print(f"e1 = ({e1[0]},{e1[1]})")
    print(f"e2 = ({e2[0]},{e2[1]})\n\n\nENCRYPTION:\n")

    print("Enter the Plaintext in terms of a point on an elliptic curve (x y, separated by space): ")
    P_Initial_input = input().split()
    P_Initial[0] = int(P_Initial_input[0])
    P_Initial[1] = int(P_Initial_input[1])

    print("Enter value of r: ")
    r = int(input())
    C1 = multiply(e1, r, a, p)
    if C1[0] < 0:
        C1[0] += p
    if C1[1] < 0:
        C1[1] += p
    C2 = addition(P_Initial, multiply(e2, r, a, p), a, p)
    if C2[0] < 0:
        C2[0] += p
    if C2[1] < 0:
        C2[1] += p

    print(f"P_Initial = ({P_Initial[0]},{P_Initial[1]})")
    print(f"C1 = ({C1[0]},{C1[1]})")
    print(f"C2 = ({C2[0]},{C2[1]})\n\n\nDECRYPTION:\n")

    temp = multiply(C1, d, a, p)
    if temp[0] < 0:
        temp[0] += p
    if temp[1] < 0:
        temp[1] += p

    print(f"(d x C1) is : ({temp[0]},{temp[1]})")

    # Adjust the inverse calculation and P_Final calculation
    tempI[1] = (p - temp[1]) % p
    tempI[0] = temp[0]
    print(f"Inverse of (d x C1) is : ({tempI[0]},{tempI[1]})")

    x1, y1 = temp[0], temp[1]
    x2, y2 = tempI[0], tempI[1]

    result = elliptic_curve_addition(x1, y1, x2, y2, a, p)

    print(f"The plain Text is: {result}")


if __name__ == "__main__":
    main()