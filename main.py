with open('ai_essay.txt' , 'w') as file:
    file.write("This was written by AI.")
file.close()

with open('ai_essay.txt' , 'r') as file:
    data = file.readlines()
    print("Words in this file are...")
    for line in data:
        word = line.split()
        print(word)
file.close()