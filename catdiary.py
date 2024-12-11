f = open("cat_diary.txt", "r")
print(f.read())

f = open("cat_diary.txt", "a")
f.write("My owner before leaving the house, played with me")
f.close()

f =open("cat_diary.txt", "r")
print(f.read())

