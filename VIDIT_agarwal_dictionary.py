import struct
print ("Welcome to dictionary")
#to generate the word and meaning and uplaod them in the dictionary 
def generate_dictionary():
    with open('dictionary.bt', 'wb') as f:
        while True:
            word = input("Enter a word or 'q' to quit/exit: ")
            if word == 'q':
                break
            meaning = input("Enter its meaning: ")
           #if the word already present then update it 
            if search_dictionary(word):
                print("The word already exists in the dictionary. Its meaning has been updated.")
           
            packed_word = word.encode('utf-8')
            packed_meaning = meaning.encode('utf-8')
            f.write(struct.pack('I', len(packed_word)))
            f.write(struct.pack('I', len(packed_meaning)))
            f.write(packed_word)
            f.write(packed_meaning)
        print("Dictionary generated successfully.")

def search_dictionary(word):
    with open('dictionary.bt', 'rb') as f:
        while True:
            try:
                word_len = struct.unpack('I', f.read(4))[0]
                meaning_len = struct.unpack('I', f.read(4))[0]
                packed_word = f.read(word_len)
                packed_meaning = f.read(meaning_len)
                if packed_word.decode('utf-8') == word:
                    return packed_meaning.decode('utf-8')
            except struct.error:
                
                break
    return None

def remove_word(word):
    with open('dictionary.bt', 'rb') as f:
       
        pairs = []
        while True:
            try:
                word_len = struct.unpack('I', f.read(4))[0]
                meaning_len = struct.unpack('I', f.read(4))[0]
                packed_word = f.read(word_len)
                packed_meaning = f.read(meaning_len)
                if packed_word.decode('utf-8') != word:
                    pairs.append((packed_word, packed_meaning))
            except struct.error:
                
                break
    with open('dictionary.bt', 'wb') as f:
       
        for pair in pairs:
            f.write(struct.pack('I', len(pair[0])))
            f.write(struct.pack('I', len(pair[1])))
            f.write(pair[0])
            f.write(pair[1])
    print(f"{word} and its meaning have been removed from the dictionary.")


while True:
    print("\nSelect an option:")
    print("1. Generate dictionary")
    print("2. Search for a word")
    print("3. Remove a word")
    print("4. Quit")
    choice = input("> ")
    if choice == '1':
        generate_dictionary()
    elif choice == '2':
        word = input("Enter a word to search: ")
        meaning = search_dictionary(word)
        if meaning:
            print(f"The meaning of '{word}' is '{meaning}'.")
        else:
            print(f"'{word}' not found in the dictionary.")
    elif choice == '3':
        word = input("Enter a word to remove: ")
        remove_word(word)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
