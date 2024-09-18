from PIL import Image
import os
import re

folder_path = r'./'

files = os.listdir(folder_path)

pattern = re.compile(r' Model: \s*(.*?)\s* Clip skip:')

for file_name in files:
    if file_name.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
        file_path = os.path.join(folder_path, file_name)

        try:
            with Image.open(file_path) as img:
                info = img.info
                info_str = str(info)
                match = pattern.search(info_str)

                if match:
                    extracted_text = match.group(1).strip()
                    # extracted_text = extracted_text.replace('\n', '')
                    # words = [word.strip() for word in extracted_text.split(',') if word.strip()]
                    # word_count = len(words)
                    print(f"File: {file_name}, Extracted Text: {extracted_text}")
                    # print(f"File: {file_name}, Extracted Text: {extracted_text}, Word Count: {word_count}")

                else:
                    print(f"File: {file_name}, No match found")
        except Exception as e:
            print(f"Failed {file_name}: {e}")
