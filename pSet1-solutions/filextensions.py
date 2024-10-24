randomInput = input("File name: ")
if ".gif" in randomInput:
    print("image/gif")
elif ".jpeg" in randomInput or ".jpg" in randomInput:
    print("image/jpeg")
elif ".png" in randomInput:
    print("image/png")
elif ".pdf" in randomInput:
    print("application/pdf")
elif ".txt" in randomInput:
    print("text/plain")
elif ".zip" in randomInput:
    print("application/zip")
else:
    print("Unknown file type")