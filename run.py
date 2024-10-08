import secrets
import os
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



def generate_api_key(length: int) -> str:
    """
    Generate a secure API key.
    """
    return secrets.token_urlsafe(length)



def main():
    key_length = int(os.getenv('KEY_LENGTH', '32'))
    logging.info(f"Generating API key with length {key_length} ...")
    api_key = generate_api_key(key_length)
    logging.info("API key generated successfully!")
    with open(os.getenv('GITHUB_OUTPUT'), 'a') as fh:
        print(f"key={api_key}", file=fh)



if __name__ == "__main__":
    main()