def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    text_lower = text.lower()
    unsorted = count_letters(text_lower)
    sorted_list = dict_to_sorted_list(unsorted)
    
    print(f"--- Report of {book_path} ---")    
    print(f"Total Number of words: {count_words(text)}")
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- report end ---")
    
    
def count_letters(text):
    letters = {"a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0, "g" : 0, "h" : 0, "i" : 0, "j" : 0, "k" : 0, "l" : 0, "m" : 0, "n" : 0, "o" : 0, "p" : 0, "q" : 0, "r" : 0, "s" : 0, "t" : 0, "u" : 0, "v" : 0, "w" : 0, "x" : 0, "y" : 0, "z" : 0}
    for letter in letters:
        letters[letter] = text.count(letter)
    return letters

def sort_on(d):
    return d["num"]

def dict_to_sorted_list(unsorted):
    sorted_list = []
    for let in unsorted:
        sorted_list.append({"char" : let, "num": unsorted[let]})
    sorted_list.sort(reverse = True, key=sort_on)
    return sorted_list
        

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)
    

main()