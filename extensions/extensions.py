b = input("File name: ").strip().lower().split('.')[-1]

if b == "jpg" or b == "jpeg":
    print("image/jpeg")
elif b == "png":
    print("image/png")
elif b == "gif":
    print("image/gif")
elif b == "pdf":
    print("application/pdf")
elif b == "txt":
    print("text/plain")
elif b == "zip":
    print("application/zip")
else:
    print("application/octet-stream")


