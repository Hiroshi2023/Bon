from huggingface_hub import HfApi, ModelCard
import os

# Récupérer les secrets depuis les variables d'environnement
hf_token = os.getenv("HF_TOKEN")
repo_id = f"{os.getenv('HF_USERNAME')}/{os.getenv('MODEL_REPO_NAME')}"

api = HfApi()
api.upload_folder(
    folder_path="hf_model",
    repo_id=repo_id,
    token=hf_token
)
