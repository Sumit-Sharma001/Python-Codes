def is_even(n: int) -> bool:
    return n % 2 == 0


def main() -> None:
    import sys

    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
        except ValueError:
            print("Please provide a valid integer as an argument.")
            sys.exit(1)
    else:
        try:
            n = int(input("Enter an integer: ").strip())
        except Exception:
            print("Invalid input. Please enter an integer.")
            sys.exit(1)

    print(f"{n} is {'even' if is_even(n) else 'odd'}")


if __name__ == '__main__':
    main()
