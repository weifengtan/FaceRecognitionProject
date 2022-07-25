import face_recognition 

image1 = face_recognition.load_image_file('./img/groups/team1.jpg')
face_locations1 = face_recognition.face_locations(image1)
image2 = face_recognition.load_image_file('./img/groups/team2.jpg')
face_locations2 = face_recognition.face_locations(image2)
image3 = face_recognition.load_image_file('./img/groups/bill-steve-elon.jpg')
face_locations3 = face_recognition.face_locations(image3)
image4 = face_recognition.load_image_file('./img/groups/bill-steve.jpg')
face_locations4 = face_recognition.face_locations(image4)
image5 = face_recognition.load_image_file('./img/groups/lotta-peeop.jpg')
face_locations5 = face_recognition.face_locations(image5)
image6 = face_recognition.load_image_file('./img/groups/bts.jpg')
face_locations6 = face_recognition.face_locations(image6)

# Print out how many people there are 
print(f'There are {len(face_locations1)} people in team1.jpg')
print(f'There are {len(face_locations2)} people in team2.jpg')
print(f'There are {len(face_locations3)} people in bill-steve-elon.jpg')
print(f'There are {len(face_locations4)} people in bill-steve.jpg')
print(f'There are {len(face_locations5)} people in lotta-peeop.jpg')
print(f'There are {len(face_locations6)} people in bts.jpg')