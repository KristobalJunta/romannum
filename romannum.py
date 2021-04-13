def rom2ar(roman):
    if type(roman) != str:
        raise TypeError

    result = 0

    nums = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    i = 0
    while i < len(roman) - 1:
        if nums[roman[i]] < nums[roman[i+1]]:
            result += nums[roman[i+1]] - nums[roman[i]]
            i += 2
        else:
            result += nums[roman[i]]
            i += 1

    if i < len(roman):
        result += nums[roman[-1]]

    return result


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        raise Exception('too few arguments')

    rom = sys.argv[1]
    print(rom2ar(rom))
