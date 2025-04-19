import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--asterisks', type=int, default=0)
    parser.add_argument('--hashtags', type=int, default=0)
    parser.add_argument('--dollars', type=int, default=0)

    args = parser.parse_args()

    for i in range(max(args.asterisks, args.hashtags, args.dollars)):
        a = '*' if i < args.asterisks else ' '
        b = '#' if i < args.hashtags else ' '
        c = '$' if i < args.dollars else ' '
        print(f"{a} {b} {c}")


if __name__ == '__main__':
    main()
