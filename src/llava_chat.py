import ollama

def chat_with_llava(image_path, prompt):
    """
    Uses the LLaVA model for inference, taking an image and a text prompt as input.
    
    :param image_path: Path to the image file.
    :param prompt: The text prompt corresponding to the image.
    :return: Model-generated text output.
    """
    res = ollama.chat(
        model="llava:13b",
        messages=[
            {
                'role': 'user',
                'content': prompt,
                'images': [image_path]
            }
        ],
        options={'temperature': 0.3},  # Set temperature to 0.5 for more deterministic output
    )
    return res['message']['content']