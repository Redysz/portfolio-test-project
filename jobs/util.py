enc_dict = {
    'a': 'Ɱ⟄⇟⚺',
    'ą': '♕⨟⠛⟑',
    'b': '⤸⎂⅍⩱',
    'c': '␛➈⨋⠹',
    'ć': 'ⶽ⍅⅁⟗',
    'd': '⻘☴⟎⽿',
    'e': 'ⴛⰌ”❕',
    'ę': 'ⶌ☹⺥▁',
    'f': '⠰⇧⛗‚',
    'g': '⬭⩚⟥╜',
    'h': '⡇☔⤀⬆',
    'i': '⣚⎞ⶄ✍ⱂ',
    'j': '∗⸗ℎ⓷',
    'k': '❳♾⏗╅',
    'l': '⇑⻠⾙⤓',
    'ł': '⌈⚇⽎⎗',
    'm': '⊌➂☻☄',
    'n': 'ⴲ⟾ⱻ➢',
    'ń': '⩺➧⸓⇂',
    'o': '⡄ⅷ⻲⧎ⷸ',
    'ó': 'ⷍ⥟ⱚⰔ',
    'p': '╇⺀Ⲫ⢃',
    'q': '↽⓼⭾⤪',
    'r': '⧢☛❡℧',
    's': '⢑✤␈⌮',
    'ś': '⊱ⵃ⮟ⲓ',
    't': '⁼⪑⣵Ⓜ',
    'u': '⛍⣯┌⨻',
    'v': '⮇ⰼ⎔⮃',
    'w': '⮠▘⢕⣠',
    'x': '➔⟪⿓⾳',
    'y': '⑳ℹ⌂⁙',
    'z': '⑺┱⁜☉',
    'ź': '◐Ⳇ⹂⬍',
    'ż': '⪥⑸⊉',

    'A': '⭟⮐≯┋',
    'Ą': '⛇◓┳⣞',
    'B': 'ⓓ⟋⾵☬',
    'C': '⩫⃪⨅➆⁃',
    'Ć': '◣⚰⌧➒',
    'D': '◒Ⱛ⣰ⴕ',
    'E': '⌗⯶⣜⍊',
    'Ę': 'ⴥ╬⚚⋣',
    'F': 'ⷀ⯆⼮ⵖ',
    'G': '♍⇻②▸',
    'H': '⼿☍✄ⲹ',
    'I': '‐⌽ⲎⲤ',
    'J': 'Ⱃ⎉⾿⣒',
    'K': '⁚┄Ȿ➏',
    'L': '≄⡣Ɽℯ',
    'Ł': '≿⩮→⚉',
    'M': '☼⪧⬘ⵎ',
    'N': '☥⁤ⳛ⨷⋾',
    'Ń': '↲Ⲗ☞⤢',
    'O': '⡆⋓ⅲ⬟',
    'Ó': '⪘⬰ⷳ⥕ⷌ',
    'P': '⼕ⴢ⍁⧖',
    'Q': '⧰⟘ℨⴟ',
    'R': '⟝ₔ⬿⢡',
    'S': '➖␢⥿⃟ⴻ',
    'Ś': '₋ⵇ⟢⥁',
    'T': 'Ɑⷒ⫀➗',
    'U': '⠾⼘⩟⏖',
    'V': '⪨⥝⩡∔',
    'W': '⬸⸮⊋⼽',
    'X': 'Ⓕ⽈⛐‡',
    'Y': '➊ⱗ⧨➉',
    'Z': '⽓∵⫋✎',
    'Ź': 'Ⰻ⢣⍦⦉',
    'Ż': '⮛ⰿⴜ⌇',

    '0': '⋊⪰⼬Ⱏ',
    '1': '∰⛏⫶ⳟ',
    '2': '⻓⡽ⷷ⽞ⰲ',
    '3': '⨺⭺⤲⼌',
    '4': '⼡Ⱜ⍥⋹',
    '5': '⼳Ⅾ╰⻑',
    '6': 'ⅉ⯍⢔Ⓑ',
    '7': 'ⶆⶁ⪊⠽',
    '8': '⬮⍈┎⡵',
    '9': '▝✼♼✽',
}

alpha = 'aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż'


def encrypt(message):
    encrypted = []
    for i, letter in enumerate(message):
        if letter in enc_dict.keys():
            encrypted.append(enc_dict[letter][i % 4])
        else:
            encrypted.append(letter)
    return ''.join(encrypted)


def decrypt(message):
    decrypted = []
    for letter in message:
        found = False
        for key, value in enc_dict.items():
            if letter in value:
                decrypted.append(key)
                found = True
                break
        if not found:
            decrypted.append(letter)
    return ''.join(decrypted)


def encrypt_rot13(message):
    encrypted = []
    length = len(alpha)
    for letter in message:
        is_upper = letter.isupper()
        letter = letter.lower()
        if letter not in alpha:
            encrypted.append(letter)
            continue
        new_letter = alpha[(alpha.find(letter) + 13) % length]
        if is_upper:
            new_letter = new_letter.upper()
        encrypted.append(new_letter)
    return ''.join(encrypted)


def decrypt_rot13(message):
    decrypted = []
    length = len(alpha)
    for letter in message:
        is_upper = letter.isupper()
        letter = letter.lower()
        if letter not in alpha:
            decrypted.append(letter)
            continue
        new_letter = alpha[(alpha.find(letter) - 13) % length]
        if is_upper:
            new_letter = new_letter.upper()
        decrypted.append(new_letter)
    return ''.join(decrypted)


def check():
    all_values = []
    repeated = 0
    for key, values in enc_dict.items():
        for value in values:
            if value in all_values:
                for key2, values2 in enc_dict.items():
                    if value in values2 and key != key2:
                        print(key, value, key2)
                        repeated += 1
        all_values += list(values)
    print(repeated == 0)

