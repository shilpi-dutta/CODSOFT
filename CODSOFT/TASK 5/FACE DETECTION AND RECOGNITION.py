def detect_photo():
    print("Photo uploaded successfully.")
    print("Object detected in the photo.")

def recognize_object(photo_type):
    photo_type = photo_type.lower()

    if photo_type == "boy":
        print("Recognition Result: This is a boy.")
    elif photo_type == "girl":
        print("Recognition Result: This is a girl.")
    elif photo_type == "dog":
        print("Recognition Result: This is a dog.")
    elif photo_type == "cat":
        print("Recognition Result: This is a cat.")
    else:
        print("Recognition Result: Unknown object.")


# Main Program
detect_photo()
user_input = input("Enter what is in the photo (boy/girl/dog/cat): ")
recognize_object(user_input)