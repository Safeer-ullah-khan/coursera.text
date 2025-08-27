# text="""Python is a powerful programming language that is easy to learn and use.Many developers love Python 
# because it is versatile and supports multiple programming paradigms. Learning Python opens the door to data science,
# web development, automation, and more, making it a valuable skill for any programmer today."""

# words=text.lower().split()

# word_count={}

# for word in words:
#     word=word.strip(".,")
#     if word not in word_count:
#         word_count[word]=1
#     else:
#         word_count[word]+=1
# print("word frequency count")
# for word,count in word_count.items():
#     print(f"{word}:{count}")
sentence="pythonismyfavoirateprogramminglanguage"


alphabet_count={}

for alphabet in sentence.upper():
    if alphabet!=" ":

     if alphabet not in alphabet_count:
         alphabet_count[alphabet]=1
     else:
         alphabet_count[alphabet]+=1
print("Alphabet Frequancy count")
for alphabet,count in sorted(alphabet_count.items()):
    print(f"{alphabet}:{count}")
