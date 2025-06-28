import numpy as np
import os
import shutil

# Relative filepaths
source_dir_AI = 'AI-1'              
destination_dir_AI = '1-AI'       

source_dir_Human = 'Human-0'              
destination_dir_Human = '0-Human'  

#Create destination directories 
os.makedirs(destination_dir_AI, exist_ok=True)
os.makedirs(destination_dir_Human, exist_ok=True)

#List all files in source directory
filesAI = [f for f in os.listdir(source_dir_AI) if os.path.isfile(os.path.join(source_dir_AI, f))]
filesHuman = [f for f in os.listdir(source_dir_Human) if os.path.isfile(os.path.join(source_dir_Human, f))]

#Select 10000 random images
num_to_select = 10000
selected_files_AI = np.random.choice(filesAI, size=num_to_select, replace=False)

num_to_select = 10000
selected_files_Human = np.random.choice(filesHuman, size=num_to_select, replace=False)

#Copy selected images to destination directory
for fname in selected_files_AI:
    src_path_AI = os.path.join(source_dir_AI, fname)
    dst_path_AI = os.path.join(destination_dir_AI, fname)
    shutil.copy2(src_path_AI, dst_path_AI)  #Preserves metadata

for fname in selected_files_Human:
    src_path_Human = os.path.join(source_dir_Human, fname)
    dst_path_Human = os.path.join(destination_dir_Human, fname)
    shutil.copy2(src_path_Human, dst_path_Human)  #Preserves metadata

print(f"Copied {len(selected_files_AI)} AI-generated images to {destination_dir_AI}")

print(f"Copied {len(selected_files_Human)} Human-made images to {destination_dir_Human}")
