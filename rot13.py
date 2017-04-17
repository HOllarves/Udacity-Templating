class Rot13():
    def process_value(self, text):

        abcd = ['a', 'b', 'c', 'd',
                'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p',
                'q', 'r', 's', 't',
                'u', 'v', 'w', 'x',
                'y', 'z']

        processed_value = ""
        capitalize = False

        if text:
            for word  in text:
                print(word)
                if word.isupper():
                    capitalize = True
                word = word.lower()
                for i, letter in enumerate(abcd):
                    if word == " ":
                        processed_value += " "
                        break
                    if word == letter:
                        index = abcd.index(letter) + 13
                        if index > 25:
                            index -= 26
                        if capitalize:
                            processed_value += abcd[index].upper()
                            capitalize = False
                            break
                        processed_value += abcd[index]
                        break
                    else:
                        if i == len(abcd) - 1:
                            processed_value += word

            return processed_value