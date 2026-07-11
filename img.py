import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
load_dotenv()

client = InferenceClient(
    provider="auto",
    api_key=os.getenv("HF_TOKE"),
)

video = client.text_to_video(
    "A young man walking on the street",
    model="Wan-AI/Wan2.2-T2V-A14B",
)
# Save the video to a local file
with open("output_video.mp4", "wb") as f:
    f.write(video)