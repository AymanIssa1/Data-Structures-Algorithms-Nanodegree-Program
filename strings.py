def string_reverser(our_string):
    new_string = ""

    for index in range(len(our_string)):
        new_string = new_string + our_string[(len(our_string) -1) - index]

    return new_string

def anagram_checker(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) == len(str2):
        if sorted(str1) == sorted(str2):
            return True

    return False

def word_flipper(our_string):
    word_list = our_string.split(" ")

    for index in range(len(word_list)):
        word_list[index] = word_list[index][::-1]

    return " ".join(word_list)

def hamming_distance(str1, str2):
    if len(str1) == len(str2):
        count = 0

        for char in range(len(str1)):
            if str1[char] != str2[char]:
                count += 1

        return count

    return None