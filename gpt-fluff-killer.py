# Import required standard libraries
import os
import re

# Specify the folder containing the .txt files to process.
# Replace the path with the location where your text files are stored.
# Use double backslashes (\\) in the folder path.
folder_path = r'your_folder_path'

# Function to remove and replace specific phrases in the text
def remove_and_replace_phrases(text, phrases_to_remove, phrases_to_replace):
    # Replace phrases in the text based on the phrases_to_replace dictionary
    for phrase, replacement in phrases_to_replace.items():
        regex_replace = re.compile(rf"\b{phrase}\b", re.IGNORECASE)
        text = regex_replace.sub(replacement, text)

    # Remove specific phrases from the text
    for phrase in phrases_to_remove:
        regex_start = re.compile(rf"^{phrase}, ", re.IGNORECASE)
        text = regex_start.sub("", text)
        regex_else = re.compile(rf"\s{phrase}(\s|,|\.)", re.IGNORECASE)
        text = regex_else.sub(" ", text)

    # Capitalize the first letter after each sentence
    text = re.sub(r"(^|\. )(.)", lambda m: m.group(1) + m.group(2).upper(), text)

    return text

# Main function to process files in a specified folder
def process_files(folder_path):
    # List of phrases to remove from the text
    phrases_to_remove = [
        "furthermore",
        "additionally",
        "in conclusion",
        "lastly",
        "therefore",
        "ultimately",
        "first and foremost"
    ]

    # Dictionary of phrases to replace in the text
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

            # Remove and replace phrases in the content
            modified_content = remove_and_replace_phrases(content, phrases_to_remove, phrases_to_replace)

            # Write the modified content to a new .txt file in the subfolder
            output_file_path = os.path.join(output_folder, filename)
            with open(output_file_path, 'w') as f:
                f.write(modified_content)

# Call the main function to start processing files
process_files(folder_path)
