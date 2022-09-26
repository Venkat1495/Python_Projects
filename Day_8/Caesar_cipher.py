alphaet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
is_true = True
while is_true :

    direction = input("Type 'encode' to encrypt or 'decode' to decrpty:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    new_text = list(text)

    def caesar_cipher_f(direction, new_text, shift):
        j = 0
        for i in new_text:
            if i in alphaet:
                t_index = alphaet.index(i)
                if direction == "encode" :
                    t_index += shift
                elif direction == "decode" :
                    t_index += 26
                    t_index -= shift
                new_text[j] = alphaet[t_index] # = alphaet[t_index]
            j += 1

        print(''.join(new_text))


    caesar_cipher_f(direction,new_text,shift)
    play_again = input("Do you want to use the program again ? type Yes - 'y' / No - 'n'")
    if play_again == 'y':
        is_true = True
    elif play_again == 'n':
        is_true = False


