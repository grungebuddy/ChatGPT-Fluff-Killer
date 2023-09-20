import os
import re

# Function to remove and replace specific phrases in the text
def remove_and_replace_phrases(text, phrases_to_remove, phrases_to_replace):
    # Replace specific phrases throughout the text
    for phrase, replacement in phrases_to_replace.items():
        text = text.replace(phrase, replacement)
        
    # Remove phrases and handle the beginning of sentences
    for phrase in phrases_to_remove:
        # If phrase is at the beginning of a sentence, remove it and the following comma
        regex_start = re.compile(rf"^{phrase}, ", re.IGNORECASE)
        text = regex_start.sub("", text)
        
        # Remove phrase if it appears elsewhere in the text
        regex_else = re.compile(rf"\s{phrase}(\s|,|\.)", re.IGNORECASE)
        text = regex_else.sub(" ", text)
        
    # Capitalize the first letter of each sentence
    text = re.sub(r"(^|\. )(.)", lambda m: m.group(1) + m.group(2).upper(), text)
    
    return text

# Main function to process files in a given folder
def process_files(folder_path):
    # Phrases to remove from the text
    phrases_to_remove = [
        "furthermore",
        "additionally",
        "in conclusion",
        "lastly",
        "therefore",
        "ultimately",
        "first and foremost"
    ]
    
    # Phrases to replace in the text
    phrases_to_replace = {
        "in addition to": "besides",
        "an informed decision": "a decision",
        "dive in": "learn about",
        "delve into": "learn about",
        "fascinating world": "topic",
        "learn about the details before making a decision": "learn more"
    }
    
    # Create a new subfolder for processed files
    output_folder = os.path.join(folder_path, "Processed_TXT")
    os.makedirs(output_folder, exist_ok=True)
    
    # Loop through each .txt file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            
            # Read the file content
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Remove and replace specified phrases
            modified_content = remove_and_replace_phrases(content, phrases_to_remove, phrases_to_replace)
            
            # Write the modified content to a new .txt file in the subfolder
            output_file_path = os.path.join(output_folder, filename)
            with open(output_file_path, 'w') as f:
                f.write(modified_content)

# Specify the folder containing the .txt files to process
# Note: Replace 'your_folder_path_here' with the actual path to your folder
# Note: Needs to use '\\'. Example: C:\\Users\\Me\\textfiles
folder_path = r'your_file_path'
process_files(folder_path)
