"""Your shy friend wants to write an anonymous note to a classmate, and they've decided to take a page from a magazine 
and cut out words to use to compose their message.
You are given two strings: one is the text from the magazine page, and one is the message that your friend wants to send. 
Determine whether your friend can send their desired message.

Example input and output:
` the bear eats shoots and leaves` , ` the bear leaves`  -> True
` the bear eats shoots and leaves` , ` the bear eats fish`  -> False

(Optional follow up):
which words are in the second message that are not in the first? In other words, which words should your friend try to replace? And what are words in the first message but not the first? In other words, which words are available for your friend to try to use? 
"""

# personal assumptions:
# something like: `the bear eats shoots and leaves`, `the bear leaves leaves` -> False because there is only one instance of "leaves"
# each "word" will be separated by a space, and no special characters like ',' or '.', '-' will disrupt our code as a precondition


# since the x amount of times a word appears in magazine does matter, hash map comes to mind
# order doesn't matter based on the problem statement
# we have to constantly check if something exists
# for simplicity, approach one: hashmap
# dp might be possible, but definitely overkill
def anonymous_note(magazine: str, message: str):
    # goal: message into hash map, iterate through magazine
    # each time we get a word thats a part of the message, we -= 1, if 0, then delete from map
    # an empty map means the magazine suffices
    message_list = message.split()
    msgMap = {}
    for msg in message_list:
        if msg in msgMap:
            msgMap[msg] += 1
        else:
            msgMap[msg] = 1
    mag_list = magazine.split()
    for magWord in mag_list:
        if magWord in msgMap:
            msgMap[magWord] -= 1
            if msgMap[magWord] == 0:
                msgMap.pop(magWord)
    return len(msgMap) == 0

if __name__ == "__main__":
    test_cases = [
        ["the bear eats shoots and leaves", "the bear leaves"],
        ["the bear eats shoots and leaves", "the bear eats fish"],
        ["the bear eats leaves", "the bear eats leaves leaves"] 
        # ^ this case shows we're short 1 "leaves" and realistically need another cut-out of leaves.
    ]
    for magazine, message in test_cases:
        print(anonymous_note(magazine, message))
