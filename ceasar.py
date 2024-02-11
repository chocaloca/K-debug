alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p',  'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

message = []
def caesar(text, shift):
  print("text: ",text,"\nshift: ",shift)
  message = list(text)
  # if shift > 26:
  #   shift = shift % 26
  count = 0
  for i in message:
    shift_new = shift
    if i in alphabet:
      print("message loop start: ",message)
      position = message.index(i)
      print("position: ",position)
      location = alphabet.index(i)
      print(" location: ",location)
  #     if direction == "decode":
  #       shift = shift * -1
      print(" shift-pre: ",shift)
      shift_new = shift + location
      if shift_new > 26:
        shift_new %= 26
      
      print(" shift post-mod: ",shift)
      
      # newlet = alphabet[location + shift]
      newlet = alphabet[shift_new] 
      print("  newlet: ",newlet)
      
      message[count]=newlet
      
      # message.insert(position,newlet)
      print("message-new:        ",message)
      # message.remove(i)
      # print("message-new-2: ",message)
      # print(message)
      count += 1
  
  
caesar(text, shift)