from PIL import Image

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = image.load()

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = image.load()

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pixels[i, j]
            # Simple decryption: Subtract key from each color channel (mod 256)
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    image.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

def main():
    print("=== Image Encryption/Decryption ===")
    choice = input("Do you want to Encrypt or Decrypt? (E/D): ").strip().upper()

    if choice not in ['E', 'D']:
        print("Invalid choice. Please enter E or D.")
        return

    image_path = input("Enter path to image: ")
    output_path = input("Enter output image path (e.g., output.png): ")
    try:
        key = int(input("Enter numeric key (e.g., 5): "))
    except ValueError:
        print("Invalid key. Please enter a number.")
        return

    if choice == 'E':
        encrypt_image(image_path, output_path, key)
    else:
        decrypt_image(image_path, output_path, key)

if __name__ == "__main__":
    main()