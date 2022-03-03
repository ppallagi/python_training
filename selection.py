#kiirja hogy helloworld mert true
if True:
    print("hello world")
print ("end")


#nem ierja ki mert false
if False:
    print("hello world")
print ("end")


#ha a név hossza nulla ird ki nem jo ne adj meg üreds nevet
name = ""
if (len(name)) == 0:
    print("ne adj meg üres nevet")


name = input("add meg a neved")
if (len(name)) == 0:
    print("ne adj meg üres nevet")



#kérd be az életkort
#ha ez kissebb mint husz ird ki hoyg tul fiatal

age = int(input("whats your age"))
if (age) < 20:
    print("too young")





