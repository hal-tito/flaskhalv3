import openpyxl
import os
import shutil
import zipfile

def change_file_extension(file_path, new_extension):
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"The file {file_path} does not exist.")
        return

    # Split the file path to get the directory and base filename
    directory, base_filename = os.path.split(file_path)

    # Generate the new file path with the new extension
    new_file_path = os.path.join(directory, os.path.splitext(base_filename)[0] + new_extension)

    # Rename the file
    os.rename(file_path, new_file_path)
    print(f"The file {file_path} has been renamed to {new_file_path}.")
    
def find_replace_in_file(file_path, find_text, replace_text):
    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Perform the find and replace operation
    new_content = content.replace(find_text, replace_text)

    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.write(new_content)
        
def zip_folder(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for foldername, subfolders, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                arcname = os.path.relpath(file_path, folder_path)
                zip_file.write(file_path, arcname)


#path_file = "E:/old pc doc/KEED_Portfolio/KEED Design/ExCodeGen/DC_DC_PID-main/DC_DC_PID.X/mcc_generated_files/tmr1.txt"
#target = "v_scale"
#new_text = "0.1221896383"
#find_replace_in_file(path_file, target, new_text)

#path_file = "E:/old pc doc/KEED_Portfolio/KEED Design/ExCodeGen/DC_DC_PID-main/DC_DC_PID.X/mcc_generated_files/tmr1.txt"
#target = "i_scale"
#new_text = "0.04887585532"
#find_replace_in_file(path_file, target, new_text)
    
#path_file = "E:/old pc doc/KEED_Portfolio/KEED Design/ExCodeGen/DC_DC_PID-main/DC_DC_PID.X/mcc_generated_files/tmr1.txt"
# Replace 'filename.txt' with your actual file and '.c' with the new extension
#change_file_extension(path_file, '.c')


workbook = openpyxl.load_workbook('Param.xlsx')
    
sheet = workbook['Sheet1']
    
cell_value = sheet['B6'].value
#    print(f'Value in cell A1: {cell_value}')
    
file_path = "E:/old pc doc/KEED_Portfolio/KEED Design/ExCodeGen/Sample_Web/DC_DC_PID-main/DC_DC_PID.X/mcc_generated_files/tmr1.txt"
target = "v_scale"
new_text = "0.1221896383"
find_replace_in_file(file_path, target, new_text)
change_file_extension(file_path, '.c')
    
    
folder_path = "E:/old pc doc/KEED_Portfolio/KEED Design/ExCodeGen/Sample_Web/DC_DC_PID-main/DC_DC_PID.X" 
zip_path = "E:/old pc doc/KEED_Portfolio/KEED Design/ExCodeGen/Sample_Web/web.zip" 
zip_folder(folder_path, zip_path)
