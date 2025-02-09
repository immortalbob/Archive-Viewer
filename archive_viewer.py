from flask import Flask, render_template, jsonify, make_response
from flask_cors import CORS
import pandas as pd
import os
import json
import math

app = Flask(__name__)
CORS(app)

# Load CSV data
df = pd.read_csv('directory.csv')

def sanitize_value(value):
    try:
        value = value.encode('utf-8').decode('utf-8', 'ignore')
    except Exception as e:
        print(f"Error sanitizing value: {e}")
        value = ""
    return value

def remove_drive_letter(path):
    if path.startswith('D:\\ACCPP\\'):
        return path[8:]  # Remove the first 8 characters "D:\ACCPP\"
    return path

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0 B"
    size_name = ("B", "KB", "MB", "GB", "TB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

def sanitize_fullname(row):
    row['FullName'] = remove_drive_letter(row['FullName'])
    if 'Length' in row and pd.notna(row['Length']):
        try:
            row['Length'] = convert_size(int(row['Length']))
        except ValueError:
            row['Length'] = 'N/A'
    return row

def build_tree(files_df):
    tree = {}
    files_df = files_df.apply(sanitize_fullname, axis=1)
    for _, row in files_df.iterrows():
        sanitized_path = row['FullName']
        parts = [part for part in sanitized_path.split(os.sep) if part]  # Filter out empty parts
        subdir = tree
        for part in parts[:-1]:
            subdir = subdir.setdefault(part, {})
        subdir[parts[-1]] = {key: sanitize_value(value) for key, value in row.items()}
    return tree

directory_tree = build_tree(df)

# Print the structure of a part of the directory tree to debug
print(json.dumps(directory_tree, indent=2, ensure_ascii=False))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/directory_tree')
def get_directory_tree():
    try:
        response = jsonify(directory_tree)
        print(json.dumps(directory_tree, indent=2, ensure_ascii=False))  # Print the JSON data to the console
        print("Directory tree successfully fetched")
        return response
    except Exception as e:
        print(f"Error fetching directory tree: {e}")
        return make_response(jsonify({'error': 'Failed to fetch directory tree'}), 500)

@app.route('/api/file_details/<path:filepath>')
def get_file_details(filepath):
    parts = filepath.split('/')
    subdir = directory_tree
    for part in parts:
        subdir = subdir.get(part, {})
    return jsonify(subdir)

if __name__ == '__main__':
    app.run(debug=True)
