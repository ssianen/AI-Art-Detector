import numpy as np
import os
import shutil
import sys
from PIL import Image
 

#Create destination directories 
os.makedirs("1-AI", exist_ok=True)
os.makedirs("0-Human", exist_ok=True)

#----------------------------------------------------------

# Absolute path to the directory this script lives in
script_dir = os.path.dirname(os.path.abspath(__file__))


# Build absolute paths
source_dir_AI_1 = os.path.join(script_dir, "AI-ArtBench", "AI")

files_AI_1 = []
count_1 = 0

for f in os.listdir(source_dir_AI_1):
    full_path_1 = os.path.join(source_dir_AI_1, f)
    try:
        with Image.open(full_path_1) as img:
            img.verify()
        
        # if full_path_1 not in files_AI_1:
            files_AI_1.append(full_path_1)

    except Exception:
        print(f"Corrupted image skipped: {full_path_1}")
        count_1 += 1
        os.remove(full_path_1)

print(f"Total valid images: {len(files_AI_1)}")
print(f"Total corrupted/skipped images: {count_1}")



source_dir_AI_2 = os.path.join(script_dir, "ai-generated-images-vs-real-images", "AI")

files_AI_2= []
count_2 = 0

for f in os.listdir(source_dir_AI_2):
    full_path_2 = os.path.join(source_dir_AI_2, f)
    try:
        with Image.open(full_path_2) as img:
            img.verify()

        # if full_path_2 not in files_AI_2:
            files_AI_2.append(full_path_2)

    except Exception:
        print(f"Corrupted image skipped: {full_path_2}")
        count_2 += 1
        os.remove(full_path_2)

print(f"Total valid images: {len(files_AI_2)}")
print(f"Total corrupted/skipped images: {count_2}")



source_dir_AI_3 = os.path.join(script_dir, "a-dataset-of-11300-labeled-ai-generated-images")

files_AI_3 = []
count_3 = 0

for f in os.listdir(source_dir_AI_3):
    full_path_3 = os.path.join(source_dir_AI_3, f)
    try:
        with Image.open(full_path_3) as img:
            img.verify()

        # if full_path_3 not in files_AI_3:
            files_AI_3.append(full_path_3)

    except Exception:
        print(f"Corrupted image skipped: {full_path_3}")
        count_3 += 1
        os.remove(full_path_3)

print(f"Total valid images: {len(files_AI_3)}")
print(f"Total corrupted/skipped images: {count_3}")



source_dir_Human_1 = os.path.join(script_dir, "AI-ArtBench", "NotAI")

files_Human_1 = []
count_4 = 0

for f in os.listdir(source_dir_Human_1):
    full_path_4 = os.path.join(source_dir_Human_1, f)
    try:
        with Image.open(full_path_4) as img:
            img.verify()

        # if full_path_4 not in files_Human_1:
            files_Human_1.append(full_path_4)

    except Exception:
        print(f"Corrupted image skipped: {full_path_4}")
        count_4 += 1
        os.remove(full_path_4)

print(f"Total valid images: {len(files_Human_1)}")
print(f"Total corrupted/skipped images: {count_4}")



source_dir_Human_2 = os.path.join(script_dir, "ai-generated-images-vs-real-images", "NotAI")

files_Human_2 = []
count_5 = 0

for f in os.listdir(source_dir_Human_2):
    full_path_5 = os.path.join(source_dir_Human_2, f)
    try:
        with Image.open(full_path_5) as img:
            img.verify()

        # if full_path_5 not in files_Human_2:
            files_Human_2.append(full_path_5)

    except Exception:
        print(f"Corrupted image skipped: {full_path_5}")
        count_5 += 1
        os.remove(full_path_5)

print(f"Total valid images: {len(files_Human_2)}")
print(f"Total corrupted/skipped images: {count_5}")




#---------------------------------------------------------------------

#Select 3000 random AI art from AI-ArtBench 
num_to_select = 3000
selected_files_AI_1 = np.random.choice(files_AI_1, size=num_to_select, replace=False)


#Select 3000 random AI images from ai-generated-images-vs-real-images
num_to_select = 3000
selected_files_AI_2 = np.random.choice(files_AI_2, size=num_to_select, replace=False)

#Select 4000 random AI images from a-dataset-of-11300-labeled-ai-generated-images 
# Note: We selected more images here becuase it is more recent AI images
num_to_select = 4000
selected_files_AI_3 = np.random.choice(files_AI_3, size=num_to_select, replace=False)

#Select 5000 random real art from AI-ArtBench
num_to_select = 7000
selected_files_Human_1 = np.random.choice(files_Human_1, size=num_to_select, replace=False)

#Select 3000 random real images from ai-generated-images-vs-real-images
num_to_select = 3000
selected_files_Human_2 = np.random.choice(files_Human_2, size=num_to_select, replace=False)

#---------------------------------------------------------------------
#Copy selected AI images to destination directory         

# Build absolute paths
destination_dir_AI = os.path.join(script_dir,"1-AI")


for src_path in selected_files_AI_1:
    dst_path = os.path.join(destination_dir_AI, os.path.basename(src_path))  # destination with just filename
    shutil.copy2(src_path, dst_path)

for src_path in selected_files_AI_2:
    dst_path = os.path.join(destination_dir_AI, os.path.basename(src_path))  # destination with just filename
    shutil.copy2(src_path, dst_path)

for src_path in selected_files_AI_3:
    dst_path = os.path.join(destination_dir_AI, os.path.basename(src_path))  # destination with just filename
    shutil.copy2(src_path, dst_path)

#---------------------------------------------------------------------
#Copy selected real images to destination directory

destination_dir_Human = os.path.join(script_dir,"0-Human")

for src_path in selected_files_Human_1:
    dst_path = os.path.join(destination_dir_Human, os.path.basename(src_path))  # destination with just filename
    shutil.copy2(src_path, dst_path)

for src_path in selected_files_Human_2:
    dst_path = os.path.join(destination_dir_Human, os.path.basename(src_path))  # destination with just filename
    shutil.copy2(src_path, dst_path)

print(f"Copied {len(selected_files_AI_1)+len(selected_files_AI_2)+len(selected_files_AI_3)} AI-generated images to {destination_dir_AI}")

print(f"Copied {len(selected_files_Human_1)+len(selected_files_Human_2)} Human-made images to {destination_dir_Human}")
