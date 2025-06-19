#先苦後甜
import sys
from os import path
if(path.exists('input.txt')):
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")

def shift_letter(letter, shift):
    if letter.isalpha():
        letter = chr(65+(ord(letter)-65+shift)%26)
    return letter

def caesar_cipher(message, shift):
    final = ""
    for i in message:
        if i.isalpha():
            final+= chr(65+(ord(i)-65+shift)%26)
        else: final+=" "
    return final 

def shift_by_letter(letter, letter_shift):
    if letter.isalpha():
        shift = ord(letter_shift)-65
        letter = chr(65+(ord(letter)-65+shift)%26)
    return letter

def vigenere_cipher(message, key):
    final = ""
    j = 0
    for i in message:
        if i == " ": final+=i
        else: 
            msgn = ord(i)-65
            keyn = ord(key[j%len(key)])-65
            final+= chr((msgn+keyn)%26+65)
        j+=1
    return final 

def scytale_cipher(message, shift):
    final = ""
    if len(message)%shift!=0:
        message+= (shift-(len(message)%shift))*"_"
    for i in range(len(message)):
        final+=message[(i//shift) + (len(message)//shift) * (i%shift)]
    return final

def scytale_decipher(message, shift):
    final = ""
    s1 = len(message)//shift
    for i in range(len(message)):
        final+=message[(i%s1)*shift+(i//s1)]
    return final