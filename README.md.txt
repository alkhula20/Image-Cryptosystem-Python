# Hybrid Image Cryptosystem in Python

A lightweight Python implementation of an image encryption algorithm designed for security research. This cryptosystem satisfies Shannon's properties of cryptography using a two-stage process:

1. **Confusion (Permutation):** Randomly scrambles the spatial pixel coordinates.
2. **Diffusion (Substitution):** Alters the RGB bit values using a seed-based deterministic XOR stream cipher.

## Requirements
- Python 3.x
- Pillow (`pip install pillow`)
- Matplotlib (`pip install matplotlib`)
