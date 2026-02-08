# Project: Coded Correspondence
# Author: Viracocha-Inti
# Project Starting message. Explains the purpose of the code.
print(
    "Hey there! How have you been? \n"
    "I've been great! I just learned about this really cool type of cipher called a Caesar Cipher. \n"
    "Here's how it works: \n"
    'You take your message, something like "hello" and then you shift all of the letters by a certain offset.'
)
print("\n")
print(
    'For example, if I chose an offset of 3 and a message of "hello", \n'
    "I would encode my message by shifting each letter 3 places to the left with respect to the alphabet. \n"
    'So "h" becomes "e", "e" becomes "b", "l" becomes "i", and "o" becomes "l". \n'
    'Then I have my encoded message, "ebiil"! \n'
    "Now I can send you my message and the offset and you can decode it by shifting each letter 3 places to the right. \n"
    "The best thing is that Julius Caesar himself used this cipher, that's why it's called the Caesar Cipher! Isn't that so cool! \n"
    "Okay, now I'm going to send you a longer encoded message that you have to decode yourself!"
)
print("\n")
print(
    "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
)
print("\n")
print("This message has an offset of 10. Can you decode it?")
print("\n")


# Function that will decode a message encoded with a simple Caesar cipher
def caesar_decode(message, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decoded_message = ""
    for character in message:
        if character in alphabet:
            letter = alphabet.index(character)
            new_letter = (letter + shift) % 26
            decoded_message += alphabet[new_letter]
        else:
            decoded_message += character
    return decoded_message


practice_encoded_message10 = "buqhd fojxed rkybt iaybbi dem"
# print(caesar_decode(practice_encoded_message10, 10))


# Function that will encode a message using a simple Caesar cipher
def caesar_encode(message, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    coded_message = ""
    for character in message:
        if character in alphabet:
            letter = alphabet.index(character)
            new_letter = (letter - shift) % 26
            coded_message += alphabet[new_letter]
        else:
            coded_message += character
    return coded_message


encoded_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
uncoded_message = "Hey Vishal!!! Long time no talk. Thanks for giving me the idea for this fun project. Hope you can decode it as well."
print("The decoded encoded message is: ")
print(caesar_decode(encoded_message, 10))
print("\n")
print("Hey Vishal, here is my coded message:")
print(caesar_encode(uncoded_message, 10))
print("\n")
print(
    "You're getting the hang of this! Okay here are two more messages, \n"
    "the first one is coded just like before with an offset of ten, and it contains a hint for decoding the second message!"
)
print("First message:")
print("jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.")
first_message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
print("Second message:")
print("bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!")
second_message = (
    "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
)
print("\n")
print("The first message is - ", (caesar_decode(first_message, 10)))
print("\n")
print("The second message is - ", (caesar_decode(second_message, 14)))
print("\n")
print(
    "Hello again friend! I knew you would love the Caesar Cipher, it's a cool, simple way to encrypt messages. \n"
    "Did you know that back in Caesar's time, it was considered a very secure way of communication and it took a lot of effort to crack if you were unaware of the value of the shift? \n"
    "That's all changed with computers! Now we can brute force these kinds of ciphers very quickly, as I'm sure you can imagine.\n"
    "Brute force this next coded message without hints\n"
    "Here's the coded message:\n"
    "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
)
print("\n")
bruto_force_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
print("Brute for message was shifted by 7:", caesar_decode(bruto_force_message, 7))
print("\n")
print(
    'Hey Viracocha, look up how the Vigenere Cipher works and then make a function that will decode my following message. Also the keyword is "friends"\n'
    "Here is the Message:\n"
    "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!"
)
