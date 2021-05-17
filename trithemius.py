import sys
import string
import argparse
from enum import Enum

alph = (string.digits + string.ascii_letters + string.punctuation +
        "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" + "№" +
        "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
step = 1

class operation(Enum):
    encode = 0
    decode = 1

def out(result):
    print("\'{}\'".format(result))
    return 0

def set_step(stp):
    global step
    step = stp

def encode(plaintext):
    i = 0
    encode_text = ""

    for index, char in enumerate(plaintext):
        global alph
        global step

        index: int = (alph.find(char) + int(step)*i) % len(alph)
        i+=1
        encode_text += alph[index]

    return encode_text

def decode(ciphertext):
    global step

    i = 0
    decode_text = ""
    for index, char in enumerate(ciphertext):
        global alph
        global step

        index: int = (alph.find(char) - int(step)*i) % len(alph)
        i+=1
        decode_text += alph[index]

    return decode_text


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Trithemius encryptor and decryptor.")

    mutexgr = parser.add_mutually_exclusive_group(required=True)
    mutexgr.add_argument(
        "-e", "--encode",
        help="defines the text for encryption",
        dest="plaintext",
        type=str
        )
    mutexgr.add_argument(
        "-d", "--decode",
        help="defines the text for decryption",
        dest="ciphertext",
        type=str
        )
    parser.add_argument(
        "-s", "--step",
        help="cryptor step",
        dest="step",
        type=int,
        required=False
        )

    args = parser.parse_args()
    op = operation(args.plaintext == None)
    if args.step is not None:
        set_step(args.step)
    # checkInput(args.step, args.plaintext, args.ciphertext)

    if op == operation.decode:
        out(decode(args.ciphertext))
    else:
        out(encode(args.plaintext))
