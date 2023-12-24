from flask import Flask, render_template, request, send_file

import openpyxl
import os
import shutil
import zipfile

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    
#    print('uploaded now')
    

    
    # Process the uploaded file with your Python code here
    # Example: Save the file to a specific location
    uploaded_file.save('uploads/' + uploaded_file.filename)
    
    workbook = openpyxl.load_workbook('Param.xlsx')
    
    sheet = workbook['Sheet1']
    
    cell_value = sheet['B6'].value
#    print(f'Value in cell A1: {cell_value}')
    
    folder_to_delete = "DC_DC_PID-main_copy"
    delete_folder(folder_to_delete)
    
    source_folder = "DC_DC_PID-main"
    destination_folder = "DC_DC_PID-main_copy"
    duplicate_folder(source_folder, destination_folder)
    
    
    file_path = "DC_DC_PID-main_copy/DC_DC_PID.X/mcc_generated_files/tmr1.txt"
    target = "v_scale"
    new_text = "0.1221896383"
    find_replace_in_file(file_path, target, new_text)
    change_file_extension(file_path, '.c')
    
    
    folder_path = "DC_DC_PID-main_copy/DC_DC_PID.X" 
    zip_path = "web.zip" 
    zip_folder(folder_path, zip_path)
    
    print('File uploaded successfully.')

    # Automatically download the generated web.zip file
    return send_file(zip_path, as_attachment=True, download_name='web.zip', mimetype='application/zip')

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

                
def delete_folder(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    
def duplicate_folder(src_folder, dest_folder):
    if os.path.exists(src_folder):
        shutil.copytree(src_folder, dest_folder)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
