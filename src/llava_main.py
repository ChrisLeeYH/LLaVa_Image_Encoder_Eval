import argparse
import os
from make_output import process_jsonl_input

def replace_input_with_output(filename):
    """
    :param filename: The input JSONL filename.
    :return: The corresponding output JSONL filename.
    """
    return filename.replace("input", "output", 1) if "input" in filename else f"output_{filename}"

def main():
    parser = argparse.ArgumentParser(description="Batch process JSONL files from an input folder and save them to an output folder")
    parser.add_argument("--input", type=str, required=True, help="Path to the folder containing input JSONL files")
    parser.add_argument("--output", type=str, required=True, help="Path to the folder where output JSONL files will be saved")

    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    input_files = [f for f in os.listdir(args.input) if f.endswith(".jsonl")]

    if not input_files:
        print("No JSONL files found in the input folder.")
        return

    for input_filename in input_files:
        input_filepath = os.path.join(args.input, input_filename)
        output_filename = replace_input_with_output(input_filename)
        output_filepath = os.path.join(args.output, output_filename)

        print(f"Processing: {input_filepath} → {output_filepath}")

        # Process each JSONL file and generate the output
        process_jsonl_input(input_filepath, output_filepath)

        print(f"Completed: {output_filepath}\n")

    print("All JSONL files in the input folder have been processed.")

if __name__ == "__main__":
    main()
