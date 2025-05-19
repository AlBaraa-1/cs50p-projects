import validator_collection


def main():
    
    email = input("What is your email address? ")
    try:
        validator_collection.validators.email(email)
        print("Valid")
    except Exception:
        print("Invalid")
    

if __name__ == "__main__":
    main()