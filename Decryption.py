import pyttsx3


class decryption:
    def __init__(self, oentext, keyword1):
        self.otext = oentext
        self.key = keyword1

    def vigeneredecipher(self, oentext, keyword1):
        key = keyword1
        kl = list(keyword1)
        entext = "".join(oentext.split())

        if len(entext) != len(keyword1):
            for i in range(len(entext) - len(keyword1)):
                key = key + kl[i]
                kl.append(kl[i])
        decipher = ""
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v",
                   "w", "x", "y", "z"]
        for i in range(len(entext)):
            num = 0
            ltpos = 0
            lkpos = 0
            if entext[i].isalpha() == True:
                if entext[i].islower() == True:
                    for j in range(len(letters)):
                        if entext[i] == letters[j]:
                            ltpos = j
                        if key[i] == letters[j]:
                            lkpos = j
                    num = int(ltpos - lkpos)
                    num = num % 26
                    decipher = decipher + letters[num]
                elif entext.isupper() == True:
                    for q in range(len(letters)):
                        letters[q] = letters[q].upper()
                    for j in range(len(letters)):
                        if entext[i] == letters[j]:
                            ltpos = j
                        if key[i] == letters[j]:
                            lkpos = j
                    num = int(ltpos - lkpos)
                    num = num % 26
                    decipher = decipher + letters[num]
            else:
                decipher = decipher + decipher[i]

        for i in range(len(oentext)):
            if oentext[i] == " ":
                decipher = decipher[:i] + " " + decipher[i:]

        print(decipher)


myobject = decryption("IHSQIRIHCQCU", "IOZQGH")
myobject.vigeneredecipher("IHSQIRIHCQCU", "IOZQGH")
speaker = pyttsx3.init()
speaker.say(myobject.decipher)
speaker.runAndWait()