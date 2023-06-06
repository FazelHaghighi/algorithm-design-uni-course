def multiply(x, y):
    # If either x or y is zero, the product is always zero.
    if x == 0 or y == 0:
        return 0
    else:
        # We first calculate the number of digits in the larger of the two numbers.
        n = max(len(str(x)), len(str(y)))
        # We then split n into two halves.
        nby2 = n // 2

        # If n is less than 2, we simply return the product of x and y.
        if n < 2:
            return x * y
        else:
            # If n is greater than 2, we split x and y into two parts each.
            # We then recursively call the multiply function with these smaller numbers.

            # We split x and y into two parts each.
            a = x // 10 ** (nby2)
            b = x % 10 ** (nby2)
            c = y // 10 ** (nby2)
            d = y % 10 ** (nby2)

            # We recursively call the multiply function with these smaller numbers.
            ac = multiply(a, c)
            bd = multiply(b, d)
            ad_plus_bc = multiply(a + b, c + d) - ac - bd

            # We combine the results to get the final product.
            prod = ac * 10 ** (2 * nby2) + (ad_plus_bc * 10**nby2) + bd

            return prod


def power(prod):
    # calculate the first digit of the product to the power of the last digit of the product.
    first_digit = int(str(prod)[0])
    last_digit = int(str(prod)[-1])
    result = first_digit**last_digit

    return result


if __name__ == "__main__":
    # We first get the input from the user.
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    # We then call the multiply function with these inputs and give the result to the power function to get the final result.
    print(power(multiply(x, y)))
