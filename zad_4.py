import argparse
from jwt import JWT
from jwt.jwk import OctetJWK
from datetime import date, datetime


def generate_token(first_name: str, second_name: str, email: str, expiry_date: str, key_str: str) -> str:
    payload = {
        'first_name': first_name,
        'second_name': second_name,
        'email': email,
        'expiry_date': expiry_date
    }

    key = OctetJWK(bytes(key_str, 'utf-8'))
    token = JWT().encode(payload, key)
    return token

def decode_token(token: str, key_str: str) -> dict:
    key = OctetJWK(bytes(key_str, 'utf-8'))
    result = JWT().decode(token, key)
    return result


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--key", required=True)
    parser.add_argument("-decode")
    parser.add_argument("-encode", action='store_true')
    parser.add_argument("--first_name")
    parser.add_argument("--second_name")
    parser.add_argument("--email")
    parser.add_argument("--expiry_date")

    args = parser.parse_args()

    if args.encode:
        if not all([args.first_name, args.second_name, args.email, args.expiry_date]):
            raise ValueError("first_name, second_name, email and expiry_date are required")
        token = generate_token(args.first_name, args.second_name, args.email, args.expiry_date, args.key)
        print(f"token=({token})")

    if args.decode:
        decoded = decode_token(args.decode, args.key)
        expiry = datetime.strptime(decoded['expiry_date'], '%d-%m-%Y').date()

        if expiry < date.today():
            print("TOKEN EXPIRED")
        else:
            print("TOKEN IS VALID")

        print(f"data={decoded}")


if __name__ == '__main__':
    main()
