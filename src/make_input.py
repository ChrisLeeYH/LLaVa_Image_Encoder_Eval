import os
import json
import argparse

def read_prompt_from_file(prompt_file):
    """
    Reads the content of a text file and returns it as a jsonl string.

    :param prompt_file: Path to the text file containing the prompt.
    :return: Prompt text as a string.
    """
    with open(prompt_file, "r", encoding="utf-8") as f:
        return f.read().strip() 

def generate_jsonl(image_folder, prompt_text, output_file):
    """
    Generates a JSONL file where each image in the folder is paired with a prompt.

    :param image_folder: Path to the folder containing images.
    :param prompt_text: The prompt text to use for all images.
    :param output_file: Path to save the generated JSONL file.
    """
    # Get all image files (supports jpg, png, jpeg, gif)
    images = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg','.gif'))]
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for image in images:
            entry = {
                "image_path": os.path.join(image_folder, image),
                "prompt": prompt_text
            }
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    print(f"Generated {output_file} with {len(images)} entries.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate multiple input JSONL files using prompts from text files")
    parser.add_argument("--image_folder", type=str, required=True, help="Path to the folder containing images")
    parser.add_argument("--prompt_files", type=str, nargs='+', required=True, help="List of text files containing prompts")

    args = parser.parse_args()

    for prompt_file in args.prompt_files:
        prompt_text = read_prompt_from_file(prompt_file)
        output_filename = f"input_{os.path.splitext(os.path.basename(prompt_file))[0]}_all_320.jsonl"
        generate_jsonl(args.image_folder, prompt_text, output_filename)