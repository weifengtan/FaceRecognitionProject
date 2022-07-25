import face_recognition
from PIL import Image, ImageDraw

image_of_bill = face_recognition.load_image_file('./img/known/Bill Gates.jpg')
bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]

image_of_steve = face_recognition.load_image_file('./img/known/Steve Jobs.jpg')
steve_face_encoding = face_recognition.face_encodings(image_of_steve)[0]

# Create an array of encodings and names 
known_face_encodings = [
    bill_face_encoding,
    steve_face_encoding
]

known_face_names = [
    "Bill Gates",
    "Steve Jobs"
]

# Load test image to find faces in 
test_image = face_recognition.load_image_file('./img/groups/bill-steve-elon.jpg')

# Find faces in test image 
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Convert to PIL format 
pil_image = Image.fromarray(test_image)

# Create a ImageDraw instance 
draw = ImageDraw.Draw(pil_image)

# Loop through faces and test image 
for(top, right, bottom, left), face_encodings in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encodings)
    
    name = "Unknown Person"

    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # Draw Box 
    draw.rectangle(((left, top), (right, bottom)), outline = (0,0,0))

    # Draw Label
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill = (0,0,0), outline = (0,0,0))
    draw.text((left + 6, bottom - text_height - 5), name, fill = (255,255,255,255))

del draw 

# Display image
pil_image.show()

# Sace image
pil_image.save('identify.jpg')