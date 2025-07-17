p1= "Make a lot of Money"
p2 = "buy now"
p3 = "subscribe this"
message = input("Enter your comment: ")
if( (p1 in message) or  (p2 in message) or  (p3 in message)):
    print("comment is spam")
else:
    print("comment is not spam")
