import argparse


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", type=float, required=True)
    parser.add_argument("-b", type=float, default=1)
    parser.add_argument("-operation", required=True,
                        choices=['add', 'sub', 'mul', 'div', 'f_div', 'mod', 'pow', 'sqrt', 'root']
                        )

    args = parser.parse_args()

    a = args.a
    b = args.b
    operation = args.operation

    text = ''

    if operation == 'add':
        text = f'{a} + {b} = {a + b}'
    elif operation == 'sub':
        text = f'{a} - {b} = {a - b}'
    elif operation == 'mul':
        text = f'{a} * {b} = {a * b}'
    elif operation == 'div':
        text = f'{a} / {b} = {a / b}'
    elif operation == 'f_div':
        text = f'{a} // {b} = {a // b}'
    elif operation == 'mod':
        text = f'{a} % {b} = {a % b}'
    elif operation == 'pow':
        text = f'{a} ** {b} = {a ** b}'
    elif operation == 'sqrt':
        text = f'sqrt({a}) = {a ** 0.5}'
    elif operation == 'root':
        text = f'{b}_root({a}) = {a ** (1/b)}'

    print(text)


if __name__ == '__main__':
    main()
