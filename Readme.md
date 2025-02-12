# Summary of All Scripts and Analysis
## Run LLaVa-Image-Encoder (./src)
1. make_input.py:
Input: prompts files, images folders.
Output: structured input jsonl files.
```json
For each line in input jsonl files,
{"image_path":"  ", "prompt":"  "}
```
2. make_output.py
Record the model answers.
Perform sturctured output jsonl files.
```json
For each line in output jsonl files,
{"image_path":"  ", "prompt":"  ", "output":"  "}
```
3. llava_chat.py
Simply deploy LLaVa model locally by Ollama.
4. llava_main.py
Main function of the LLaVa-Image-Encoder.
Input: input jsonl files.
Output: output jsonl files.

## Analyze (./Eval)
(update: ipynb files are converted to html files)
1. parse_output.ipynb:
parse the output files and extract the interesting strings.
2. analysis.ipynb:
a statistical and empirical analysis to evaluate the performance of LLaVa rating.

## Data (./Data)
Contains all raw (link) and generated data.
