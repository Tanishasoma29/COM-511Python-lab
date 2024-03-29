MORSE_CODE_DICT ={
'A':'.-', 'B':'-...', 'C':'-.-', 'D':'-..', 'E':'.', 'F':'..-.','G':'--.', 'H':'....','I':'..', 
'J':'.---', 'K':'-.-','L':'.-..','M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 
'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----
', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', 
'0': '-----', ' ':'/'
}
def text_to_morse(text):
morse_code=''
for char in text.upper():
if char in MORSE_CODE_DICT:
morse_code += MORSE_CODE_DICT[char] + ' '
else:
morse_code += char + ' '
return morse_code.strip()
def morse_to_text(morse_code):
morse_code = morse_code.split(' ')
text = ''
for code in morse_code:
for key,value in MORSE_CODE_DICT.items():
if code==value:
text+=key
return text
def main():
print("Morse Code Translator")
choice = input("1. Text to morse code translation\n2. Morse to text 
Translation\n Enter choice: ")
if choice=='1':
input_text = input("Enter the text to translate to Morse code: ")
result = text_to_morse(input_text)
print(f"Morse Code: {result}")
elif choice=='2':
input_morse = input("Enter the Morse code to translate to 
text(use space between Morse code symbols): ")
result = morse_to_text(input_morse)
print(f"Text: {result}")
else:
print("Invalid choice. Please enter '1' or '2'")
if __name__=="__main__":
main()
