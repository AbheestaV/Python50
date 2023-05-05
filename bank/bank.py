a = input("Greeting: ").strip().lower()
#print(a[:5])
if a[:5] == "hello":
    print("$0")
elif a[0] == "h":
    print("$20")
else:
    print("$100")