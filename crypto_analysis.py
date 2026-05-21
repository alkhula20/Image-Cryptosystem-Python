"""
Cryptosystem Histogram Analysis Module
Author: Mohad
Description: Extracts and plots grayscale or RGB color histograms 
             to evaluate the diffusion properties of an image cipher.
"""

import matplotlib.pyplot as plt
from PIL import Image

def analyze_color_histogram(original_path, encrypted_path, output_chart_path="histogram_analysis.png"):
    """
    Plots and saves RGB histograms for color images to verify uniform distribution.
    """
    try:
        orig_img = Image.open(original_path).convert("RGB")
        enc_img = Image.open(encrypted_path).convert("RGB")

        orig_r, orig_g, orig_b = orig_img.split()
        enc_r, enc_g, enc_b = enc_img.split()

        fig, axes = plt.subplots(2, 2, figsize=(12, 8))
        fig.suptitle("RGB Cryptosystem Histogram Analysis", fontsize=14, fontweight='bold')

        # Original Layout
        axes[0, 0].imshow(orig_img)
        axes[0, 0].set_title("Original Image")
        axes[0, 0].axis("off")

        axes[0, 1].hist(orig_r.getdata(), bins=256, color="red", alpha=0.4, label="Red")
        axes[0, 1].hist(orig_g.getdata(), bins=256, color="green", alpha=0.4, label="Green")
        axes[0, 1].hist(orig_b.getdata(), bins=256, color="blue", alpha=0.4, label="Blue")
        axes[0, 1].set_title("Original RGB Distribution")
        axes[0, 1].legend()

        # Encrypted Layout
        axes[1, 0].imshow(enc_img)
        axes[1, 0].set_title("Encrypted Image")
        axes[1, 0].axis("off")

        axes[1, 1].hist(enc_r.getdata(), bins=256, color="red", alpha=0.4, label="Red")
        axes[1, 1].hist(enc_g.getdata(), bins=256, color="green", alpha=0.4, label="Green")
        axes[1, 1].hist(enc_b.getdata(), bins=256, color="blue", alpha=0.4, label="Blue")
        axes[1, 1].set_title("Encrypted RGB Distribution (Uniform)")
        axes[1, 1].legend()

        plt.tight_layout()
        plt.savefig(output_chart_path)
        print(f"[+] Histogram plot successfully saved to: {output_chart_path}")
        plt.close()
        return True
    except Exception as e:
        print(f"[-] Error during color histogram analysis: {e}")
        return False

def analyze_grayscale_histogram(original_path, encrypted_path, output_chart_path="xray_histogram_analysis.png"):
    """
    Plots and saves intensity histograms for grayscale images (e.g., X-rays).
    """
    try:
        orig_img = Image.open(original_path).convert("L")
        enc_img = Image.open(encrypted_path).convert("L")

        fig, axes = plt.subplots(2, 2, figsize=(12, 8))
        fig.suptitle("Grayscale Cryptosystem Histogram Analysis", fontsize=14, fontweight='bold')

        # Original Layout
        axes[0, 0].imshow(orig_img, cmap='gray')
        axes[0, 0].set_title("Original Grayscale Image")
        axes[0, 0].axis("off")

        axes[0, 1].hist(orig_img.getdata(), bins=256, color="black", alpha=0.7)
        axes[0, 1].set_title("Original Intensity Distribution")

        # Encrypted Layout
        axes[1, 0].imshow(enc_img, cmap='gray')
        axes[1, 0].set_title("Encrypted Grayscale Image")
        axes[1, 0].axis("off")

        axes[1, 1].hist(enc_img.getdata(), bins=256, color="gray", alpha=0.7)
        axes[1, 1].set_title("Encrypted Intensity Distribution (Uniform)")

        plt.tight_layout()
        plt.savefig(output_chart_path)
        print(f"[+] Histogram plot successfully saved to: {output_chart_path}")
        plt.close()
        return True
    except Exception as e:
        print(f"[-] Error during grayscale histogram analysis: {e}")
        return False
