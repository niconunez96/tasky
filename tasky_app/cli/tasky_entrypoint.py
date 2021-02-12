import argparse


parser = argparse.ArgumentParser()

parser.add_argument("-a", "--add", help="Add a new task", type=str)
parser.add_argument("-l", "--list", help="List all tasks", action="store_true")
parser.add_argument("-s", "--select", help="Select one task", type=int)

# args = parser.parse_args()

# print(args.add)
# print(args.list)
# print(args.select)
