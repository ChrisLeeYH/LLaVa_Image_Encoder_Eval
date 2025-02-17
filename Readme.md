# Summary of All Scripts and Analysis （Updated Version: Feb 18th, 2025）
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
**To control the randomness of LLaVa, "Temperature==0.3" is added.**
4. llava_main.py
Main function of the LLaVa-Image-Encoder.
Input: input jsonl files.
Output: output jsonl files.

## Analyze (./Eval)
(update: ipynb files are converted to html files)
1. parse_output.ipynb:
parse the output files and extract the interesting strings.
2. analysis.ipynb:
2.1 a statistical and empirical analysis to evaluate the performance of LLaVa rating. 
2.2 additional Results are added in analysis.ipynb, including more correlation, MAE and MSE analyses Between Human ratings and LLM average ratings in ten scenarios. (See folder ./Additional Results)
```
The correlation, MAE, and MSE between human ratings and LLM-generated ratings arecomputed for different scenarios in Additional Results:

Human against one LLM rating

...The average of two LLM ratings

...The average of three LLM ratings

… all the way up to ten LLM ratings
```

## Data (./Data)
Contains all raw (link) and generated data.
"Data\with_temperature\parsed_output_all_320_temperature_0.3\Mean_Folder" shows all average LLM ratings in total ten scenarios, 
```
i.e. Only one LLM rating

...The average of two LLM ratings

...The average of three LLM ratings

...The average of ten LLM ratings
```
