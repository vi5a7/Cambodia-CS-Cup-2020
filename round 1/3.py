def caecar_cipher(s, shift):
    text=""
    for i in s:
        if ord(i)-shift>96:
            i = chr(ord(i)-shift)
        else:
            i = chr(ord(i)-97+123-shift)
        text+=i
    return text

if __name__ == '__main__':
    s = input()
    shift = ord(s[0]) - ord('a')
    print(caecar_cipher(s,shift))