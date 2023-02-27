import cv2
import argparse

# We will first create the ArgumentParser object
# The created object 'parser' will have the necessary information.
# To parse the command-line arguments into data types

parser = argparse.ArgumentParser()


parser.add_argument(
    "--number1", help="this is the string text in connection with first_argument", default=8)
parser.add_argument(
    "--number2", help="this is the string text in connection with second_argument", default=10)
parser.add_argument(
    "--operation", help="operation", choices=["add", "subtract", "multiply"], default="add")


# The information about program arguments is stored in 'parser' and used when parse_args is called.
# ArgumentParser parses arguments through the parse_args() method:
args = parser.parse_args()


print(args.number1)
print(args.number2)
print(args.operation)

n1 = int(args.number1)
n2 = int(args.number2)

results = None

if args.operation == "add":
    results = n1+n2
elif args.operation == "subtract":
    results = n1-n2
elif args.operation == "multiply":
    results = n1*n2

print(f"Result is: {results}")
