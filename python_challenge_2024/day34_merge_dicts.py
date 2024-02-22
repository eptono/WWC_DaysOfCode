#-------------------------------------------------------------------------------
# Day 34: Write a Python program to merge two dictionaries
#
# The merging functionality in this programs gives the user three choices in
# case of keys occurring in both dictionaries:
#    - keep both values (in format {key: [value1, value2]})
#    - delete the key
#    - choose case by case which value to keep.

#-------------------------------------------------------------------------------

def conscious_merge(d1, d2):

    d3 = {**d1, **d2} # simple merge functionality

    delete_lst = []
    setting = ""

    # Checking for double keys
    for key, value in d3.items():

        if key in d1 and key in d2:

            # The user will be asked once about the preferred setting
            if setting == "":
                setting = ask_setting()

            # Performing the chosen setting
            if setting == 'k':
                d3[key] = [d1[key], d2[key]]

            elif setting == 'd':
                delete_lst.append(key)

            elif setting == 'i':
                keep = ask_keep(key, d1[key], d2[key])

                if keep == '1':
                    d3[key] = d1[key]

                elif keep == '2':
                    d3[key] = d2[key]

    if delete_lst:
        for key in delete_lst:
            del d3[key]

    return d3


def ask_setting():
    '''Asks the user to choose a behaviour in case of double keys. Valid input
    is 'k' (keep both values), 'd' (delete the key from the merged dictionary)
    or 'i' (decide individually).'''

    while(True):

        setting = input("Double keys detected. Choose one of the following settings: \n\
            Keep both values: press 'k' \n\
            Delete all double keys: press 'd' \n\
            Decide individually for each case of double keys: press 'i'")

        if not setting in ["k", "d", "i"]:
            continue
        else:
            break

    return setting


def ask_keep(key, value1, value2):
    '''Asks the user which value to keep in case of a double key.'''

    while(True):

        keep = input("Key '{key}' is in both dictionaries. \n\
            Keep value '{value1}': press 1 \n\
            Keep value '{value2}': press 2 \n\ "
            .format(key=key, value1=value1, value2=value2))

        if keep not in ["1","2"]:
            continue
        else:
            break

    return keep


def main():

    d1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}
    d2 = {'a':9, 'b':13, 'c':10, 'e':12, 'f':11, 'g':7, 'h':8}

    print(conscious_merge(d1, d2))


if __name__ == '__main__':
    main()
