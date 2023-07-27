import random


def icc_generator(chars, icclength):
    # Unpacks the valid letters and numbers for icc
    charlst = set(chars)
    # We can also use this below but we will use set to avoid duplicates
    # lst = [x for x in chars]

    # Stores the generated icc
    icc = []

    # Repeats the iteration for 4 times (0, 1, 2, 3)
    for y in range(4):
        # Combines the chars and numbers that is only valid
        # The length k varies
        str = "".join(random.choices(list(charlst), k=icclength))

        # Adds / appends the generated 4 character long into the icc list
        icc.append(str)

    # Returns the value from the icc list by joining them with a '-'
    return "-".join(icc)
