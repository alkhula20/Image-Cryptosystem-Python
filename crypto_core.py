"""
Two-Stage Chaos-Based Hybrid Image Cryptosystem
Author: Mohad
Description: A research-grade image encryption system combining 
             Position Permutation (Confusion) and Bitwise XOR Diffusion (Substitution).
"""

import random
from PIL import Image

def encrypt_image(image_path, output_path, secret_key):
    """
    Encrypts a color or grayscale image using hybrid permutation and diffusion.
    """
    try:
        img = Image.open(image_path).convert("RGB")
        pixels = img.load()
        width, height = img.size

        coordinates = [(x, y) for x in range(width) for y in range(height)]
        original_colors = [pixels[x, y] for x, y in coordinates]

        shuffled_indices = list(range(len(coordinates)))
        random.seed(secret_key)
        random.shuffle(shuffled_indices)

        encrypted_img = Image.new("RGB", (width, height))
        enc_pixels = encrypted_img.load()

        for idx, (orig_r, orig_g, orig_b) in enumerate(original_colors):
            noise_r = random.randint(0, 255)
            noise_g = random.randint(0, 255)
            noise_b = random.randint(0, 255)

            xor_r = orig_r ^ noise_r
            xor_g = orig_g ^ noise_g
            xor_b = orig_b ^ noise_b

            target_coords = coordinates[shuffled_indices[idx]]
            enc_pixels[target_coords] = (xor_r, xor_g, xor_b)

        encrypted_img.save(output_path)
        print(f"[+] Encryption Successful: Saved to {output_path}")
        return True
    except FileNotFoundError:
        print(f"[-] Error: Source image not found at {image_path}")
        return False

def decrypt_image(scrambled_path, output_path, secret_key):
    """
    Decrypts an image encrypted by the hybrid system back to its original form.
    """
    try:
        img = Image.open(scrambled_path).convert("RGB")
        pixels = img.load()
        width, height = img.size

        coordinates = [(x, y) for x in range(width) for y in range(height)]
        
        shuffled_indices = list(range(len(coordinates)))
        random.seed(secret_key)
        random.shuffle(shuffled_indices)

        restored_img = Image.new("RGB", (width, height))
        restored_pixels = restored_img.load()

        for idx, original_coord in enumerate(coordinates):
            scrambled_coords = coordinates[shuffled_indices[idx]]
            scr_r, scr_g, scr_b = pixels[scrambled_coords]

            noise_r = random.randint(0, 255)
            noise_g = random.randint(0, 255)
            noise_b = random.randint(0, 255)

            true_r = scr_r ^ noise_r
            true_g = scr_g ^ noise_g
            true_b = scr_b ^ noise_b

            restored_pixels[original_coord] = (true_r, true_g, true_b)

        restored_img.save(output_path)
        print(f"[+] Decryption Successful: Saved to {output_path}")
        return True
    except FileNotFoundError:
        print(f"[-] Error: Encrypted image not found at {scrambled_path}")
        return False
