import argparse
import sys


def a(x):
    return x


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="test parser")
    parser.add_argument("--model_key", type=str, help="Model key")
    args = parser.parse_args()
    if args.model_key is None:
        parser.print_help(sys.stderr)
        sys.exit(1)
    print(args.model_key)
