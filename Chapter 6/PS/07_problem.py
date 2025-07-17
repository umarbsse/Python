post= input("Enter the post")
word = "python"
if(word.lower() in post.lower()):
    print("This post talking about",word)
else:
    print("This post does not talking about", word)