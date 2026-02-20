from constants import *


def load_file_entries(reg, mem, disk_name):
    """
    Load the directory entries for files into memory at
    `FILE_DIRECTORY_BASE`.

    Assumes disk is a continuous array of 24-bit hex digits, space o
    whitespace separated
    """

    current_word = 0
    with open(disk_name) as f:
        while current_word < F_DIRECTORY_SIZE:
            line = f.readline().split()
            if not line: break
            for i, word in enumerate(line):
                if current_word == F_DIRECTORY_BASE: break
                mem[F_DIRECTORY_BASE + current_word] = int(word, 16)
                current_word += 1
