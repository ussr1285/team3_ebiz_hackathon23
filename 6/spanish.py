def check_available(string):
    for raw_char in string:
        char = ord(raw_char)
        if(not(raw_char == ',' or raw_char == '.' or raw_char == '~' or (char >= 97 and char <= 122))):
            # print(raw_char, char)
            return(False)

def spanish_len(string):
    if(check_available(string) == False):
        return(False)
    string = string.replace("a,", "á")
    string = string.replace("e,", "é")
    string = string.replace("i,", "í")
    string = string.replace("n~", "ñ")
    string = string.replace("o,", "ó")
    string = string.replace("u,", "ú")
    string = string.replace("u..", "ü")
    # print(string)
    return(len(string))

user_input = input("Plesae enter spanish: ")
value = spanish_len(user_input)
if(value == False):
    print("입력은 영어 소문자와 , . ~ 로만 사용해주세요.")
else:
    print("스페인어 길이:", value)
