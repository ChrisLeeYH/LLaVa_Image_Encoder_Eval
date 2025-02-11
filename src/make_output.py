import json
from llava_chat import chat_with_llava

def process_jsonl_input(input_file, output_file, repeat=10):
    """
    Reads the JSONL input file, sends each entry to LLaVA 'repeat' times, 
    and writes multiple outputs to the JSONL output file.

    :param input_file: JSONL input file containing image_path and prompt.
    :param output_file: JSONL file to store outputs.
    :param repeat: Number of times each input should be sent to the model.
    """
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        total_images = sum(1 for _ in infile)
        infile.seek(0)  # Reset file pointer to the beginning

        processed_images = 0

        for line in infile:
            data = json.loads(line.strip())
            image_path = data["image_path"]
            prompt = data["prompt"]
            
            for i in range(repeat):
                model_output = chat_with_llava(image_path, prompt)

                result = {
                    "image_path": image_path,
                    "prompt": prompt,
                    "output": model_output
                }
                outfile.write(json.dumps(result, ensure_ascii=False) + "\n")

            # Print progress update after finishing 10 outputs for one image
            processed_images += 1
            print(f"Processed {processed_images}/{total_images}: {image_path}")

    print(f"Processing completed.")
