import os

IGNORE_FOLDER=['images','labels']
FILE_PATH = os.path.realpath(__file__)
CURRENT_FOLDER = os.path.dirname(FILE_PATH)

images_to_move = []
labels_to_move = [] 

### Get all the images to move 
for results in os.listdir(CURRENT_FOLDER):    
  if results not in IGNORE_FOLDER and os.path.isdir(os.path.join(CURRENT_FOLDER,results)):
      current_folder_path = os.path.join(CURRENT_FOLDER,results)
      files = [os.path.join(current_folder_path,files) for files in os.listdir(current_folder_path) if files.endswith('.jpg')  ]
      images_to_move.extend(files)


### Get all the labels to move

print(len(images_to_move))


