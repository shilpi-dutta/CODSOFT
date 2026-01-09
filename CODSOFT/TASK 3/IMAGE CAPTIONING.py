def image_captioning(image_name):
    image_name = image_name.lower()

    if "dog" in image_name:
        caption = "A dog is sitting happily."
    elif "cat" in image_name:
        caption = "A cat is resting calmly."
    elif "car" in image_name:
        caption = "A car is parked on the road."
    elif "person" in image_name:
        caption = "A person is standing and posing."
    elif "tree" in image_name:
        caption = "A green tree is under the sky."
    else:
        caption = "This is an image with some objects."

    return caption


image = input("Enter image name: ")
print("Generated Caption:", image_captioning(image))