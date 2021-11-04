def syllables(palabra):
    palabra = palabra.lower()
    palabra = palabra + " "  # palabra extended
    length = len(palabra)
    termina = ["ing ", "ed ", "es ", "ous ", "tion ", "nce ", "ness ","on"]  # not included in complex palabras
    vocales = "aeiouy"

    for end in termina:
        x = palabra.find(end)
        if x > -1:
            x = length - x
            palabra = palabra[:-x]
    conteo_silaba = 0
    if palabra[-1] == " ":
        palabra = palabra[:-1]
    # removing the extra " " at the end if failed and dropping last letter if e
    if palabra[-1] == "e":
        try :
            if palabra[-3:] == "nce" and palabra[-3:] == "rce":
                conteo_silaba = 0

            elif palabra[-3] not in vocales and palabra[-2] not in vocales and palabra[-3:] != "nce" and palabra[-3:] != "rce":
                if palabra[-3] != "'":
                    conteo_silaba += 1  # e cannot be dropped as it contributes to a syllable
            palabra = palabra[:-1]
        except IndexError:
            conteo_silaba += 0

    one_syllable_beg = ["ba","be","bi","bo","bu","ca","ce","ci","cu","da","de","di","do","du",
    "fa","fe","fi","fo","fu", "ga","ge","gi","go","gu","ha","he","hi","ho","hu","ja","je","ji",
    "jo","ju","la","le","li","lo","lu","ma","me","mi","mo","mu","na","ne","ni","no","nu","pa",
    "pe","pi","po","pu","ra","re","ri","ro","ru","sa","se","si","so","su","ta","te","ti","to",
    "tu","va","ve","vi","vo","vu","xa","xe","xi","xo","xu","za","ze","zi","zo","zu","ya",
     "ae", "oe", "ea"]
    two_syllables = ["ae","ai","ao","au","ea","ei","eo","eu","ia","ie","io","iu",
    "oa","oe","oi","ou","ua","ue","ui","uo", "uu", "eous", "uou", "ii", "ya", "yo", "yu", "ye"]
    last_letter = str()  # last letter is null for the first alphabet
    for index, alphabet in enumerate(palabra):
        if alphabet in vocales:
            current_combo = last_letter + alphabet
            if len(current_combo) == 1:  # if it's the first alphabet
                if palabra[1] not in vocales:  # followed by a consonant, then one syllable
                    conteo_silaba += 1
                    last_letter = palabra[1]
                else:
                    conteo_silaba += 1  # followed by a vowel
                    last_letter = alphabet

            else:
                if current_combo in two_syllables:
                    try:
                    # if they're only 1 syllable at the beginning of a palabra, don't increment
                        if current_combo == palabra[:2] and current_combo in one_syllable_beg:
                            conteo_silaba += 0
                        elif palabra[index - 2] + current_combo + palabra[index + 1] == "tion" or palabra[index - 2] + current_combo + \
                                palabra[index + 1] == "sion":  # here io is one syllable :
                            conteo_silaba += 0

                        else:
                            conteo_silaba += 1  # vowel combination forming 2 syllables

                        last_letter = alphabet
                    except IndexError:
                        conteo_silaba += 0

                else:  # two vocales as well as non vowel combination
                    if last_letter not in vocales:
                        conteo_silaba += 1
                        last_letter = alphabet

                    else:
                        last_letter = alphabet


        else:
            last_letter = alphabet

    if palabra[-3:] == "ier" or "uo":  # palabra termina with ier has 2 syllables
        conteo_silaba += 1

    return conteo_silaba