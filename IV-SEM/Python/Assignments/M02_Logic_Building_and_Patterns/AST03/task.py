def sum_of_digits(n: int) -> int:
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

if __name__ == "__main__":
    n = int(input())
    print(sum_of_digits(n))
