import re


class HashMap:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size

    def __str__(self):
        pairs = []
        for i in range(self.size):
            if self.map[i]:
                for pair in self.map[i]:
                    pairs.append(f"{pair[0]}: {pair[1]}")
        return "\n".join(pairs)

    def __len__(self):
        count = 0
        for i in range(self.size):
            if self.map[i]:
                count += len(self.map[i])
        return count

    def __contains__(self, key):
        slot = self.hashfunction(key)
        if self.map[slot]:
            for pair in self.map[slot]:
                if pair[0] == key:
                    return True
        return False

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __delitem__(self, key):
        self.remove(key)

    def hashfunction(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        slot = self.hashfunction(key)
        if not self.map[slot]:
            self.map[slot] = []
        for i, pair in enumerate(self.map[slot]):
            if pair[0] == key:
                self.map[slot][i] = (key, value)
                return
        self.map[slot].append((key, value))

    def get(self, key):
        slot = self.hashfunction(key)
        if self.map[slot]:
            for pair in self.map[slot]:
                if pair[0] == key:
                    return pair[1]
        return -1

    def remove(self, key):
        slot = self.hashfunction(key)
        if self.map[slot]:
            for i, pair in enumerate(self.map[slot]):
                if pair[0] == key:
                    del self.map[slot][i]
                    return slot
        return -1


def clean_word(word):
    return re.sub(r"[^a-zA-Z0-9']", "", word.lower())


def count_words(file_name):
    # create the map
    map = HashMap()
    #initialize count
    total_count = 0

    #open file as read
    with open(file_name, "r") as f:
        #for every line in f split the line into words
        for line in f:
            words = line.split()
            #for every word in the line
            for word in words:
                #clean the word i.e., substitute all the occurences in every word with a null character and basically removing any non-alphanumeric character
                clean_words = clean_word(word)
                #if clean_words is not empty that is if it has any alphanumeric character
                if clean_words:
                    #if it is in our hashmap then increase its occurence value
                    if clean_words in map:
                        map[clean_words] += 1
                    else:
                        #if is not in our map already then we initialize it
                        map[clean_words] = 1
                    total_count += 1

    print(f"total count: {total_count}")
    #run the counter until the user inputs q
    while True:
        word = input("Try a word (enter 'Q' or 'q' to quit): ")
        if word.lower() == "q":
            break
        count = map.get(clean_word(word))
        if count != -1:
            print(f"Word '{word}' has a count of {count}")
        else:
            print(f"Word '{word}' not found")

def main():
    count_words("moby_start.txt")
    count_words("moby_end.txt")
if __name__=='__main__':
    main()