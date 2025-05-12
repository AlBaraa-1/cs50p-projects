def main():
    #take file name from the user
    userInput = input("File name:\n").strip().lower()

    #split the input by dot and store it in a list
    fileExtension = userInput.split(".")
    
    #check the file extension and print the corresponding mime type
    if fileExtension[-1] == "gif":
        print("image/gif")
    elif fileExtension[-1] == "jpg" or fileExtension[-1] == "jpeg":
        print("image/jpeg")
    elif fileExtension[-1] == "png":
        print("image/png")
    elif fileExtension[-1] == "pdf":
        print("application/pdf")
    elif fileExtension[-1] == "txt":
        print("text/plain")
    elif fileExtension[-1] == "zip":
        print("application/zip")
    else:
        print("application/octet-stream")


if __name__ == "__main__":
    main()
    