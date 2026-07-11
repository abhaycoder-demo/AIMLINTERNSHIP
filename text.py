# from transformers import pipeline

# text= "I didn't like the movie , it was disappointing." 

# classifier = pipeline('sentiment-analysis')
# result= classifier(text
# predicted_label = result[0]['label']
# cofidence_score = result[0]['score']

# if predicted_label == 'NEGATIVE':
#     print(f"The sentiment of the text is Negative with a confidence score of {cofidence_score:.4f}")
# else:
#     print(f"The sentiment of the text is Positive with a confidence score of {cofidence_score:.4f}")
import requests
import io
from PIL import Image
import random

def generate_image(prompt):
    # Add a random seed to ensure the image changes if you run it twice
    seed = random.randint(1, 10000)
    
    # We force 'model=turbo' to avoid the 500 error on Flux
    url = f"https://image.pollinations.ai/prompt/{prompt}?model=turbo&seed={seed}"
    
    print(f"Requesting: {url}")
    response = requests.get(url)
    
    if response.status_code == 200:
        image = Image.open(io.BytesIO(response.content))
        image.show()
        print("Image generated successfully!")
    else:
        print(f"Error: {response.status_code} - {response.text}")

# Usage
generate_image("A humanoid AI robot working in a futuristic laboratory, holographic screens, blue glowing eyes, realistic metal textures, cinematic lighting, ultra detailed, 8k.")