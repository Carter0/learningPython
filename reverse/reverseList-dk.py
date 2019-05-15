#!/usr/bin/env python3
import argparse


def naive_reverse(input_list: [str]):
    new_list = []
    size = len(input_list) - 1
    for i in range(0, len(input_list)):
        new_list.append(input_list[size - i])
    return new_list


def ergonomic_reverse(input_list: [str]):
    return input_list[::-1]


if __name__ == "__main__":
    # print(ergonomic_reverse(["logs", "want", "to", "be", "happy"]))
    argsparsed = argparse.ArgumentParser(description='Reverse dem Lists')
    argsparsed.add_argument(
        '-n', '--naive', help='A naive implementation of reversing', type=str)
    argsparsed.add_argument(
        '-f', '--fn', help='Python\'s fancy reversing syntax', type=str)

    args = argsparsed.parse_args()
    if args.naive:
        inpt = list(args.naive.split(','))
        print(naive_reverse(inpt))
    elif args.fn:
        inpt = list(args.fn.split(','))
        print(ergonomic_reverse(inpt))
    else:
        print("Enter a valid input.")
