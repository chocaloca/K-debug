alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p',  'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

message = []
def caesar(text, shift):
  message = list(text)
  # if shift > 26:
  #   shift = shift % 26
  count = 0
  for i in message:
    shift_new = shift
    if i in alphabet:
      position = message.index(i)
      location = alphabet.index(i)
  #     if direction == "decode":
  #       shift = shift * -1
      shift_new = shift + location
      if shift_new > 26:
        shift_new %= 26

      # newlet = alphabet[location + shift]
      newlet = alphabet[shift_new] 
      message[count]=newlet
      # message.insert(position,newlet)
      # message.remove(i)
      print(message)
      count += 1
  
  
caesar(text, shift)