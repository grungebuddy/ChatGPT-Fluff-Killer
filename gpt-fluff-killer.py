import os
import re

# Function to remove and replace specific phrases in the text
def remove_and_replace_phrases(text, phrases_to_remove, phrases_to_replace):
    for phrase, replacement in phrases_to_replace.items():
        text = text.replace(phrase, replacement)
        
    for phrase in phrases_to_remove:
        regex_start = re.compile(rf"^{phrase}, ", re.IGNORECASE)
        text = regex_start.sub("", text)
        
        regex_else = re.compile(rf"\s{phrase}(\s|,|\.)", re.IGNORECASE)
        text = regex_else.sub(" ", text)
        
    text = re.sub(r"(^|\. )(.)", lambda m: m.group(1) + m.group(2).upper(), text)
    
    return text

# Main function to process files in a given folder
def process_files(folder_path):
    phrases_to_remove = [
        "furthermore",
        "additionally",
        "in conclusion",
        "lastly",
        "therefore",
        "ultimately",
        "in addition"
    ]
    
    phrases_to_replace = {
        "in addition to": "besides",
        "an informed decision": "a decision",
        "dive in": "learn about",
        "delve into": "learn about",
        "fascinating world": "topic",
        "learn about the details before making a decision": "learn more"
    }
    
    output_folder = os.path.join(folder_path, "Processed_TXT")
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            
            with open(file_path, 'r') as f:
                content = f.read()
            
            modified_content = remove_and_replace_phrases(content, phrases_to_remove, phrases_to_replace)
            
            output_file_path = os.path.join(output_folder, filename)
            with open(output_file_path, 'w') as f:
                f.write(modified_content)

# Specify the folder containing the .txt files to process.
# Note: Use double backslashes (\\) in the folder path for Python to interpret it correctly.
folder_path = r'your_folder_path_here'
process_files(folder_path)
