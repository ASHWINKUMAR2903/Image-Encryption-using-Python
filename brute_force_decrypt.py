import os

SIGNATURES = {
    "JPEG": bytes.fromhex("FFD8FF"),
    "PNG": bytes.fromhex("89504E470D0A1A0A")
}

def brute_force_decrypt(image_path):
    # Read the encrypted image
    with open(image_path, "rb") as file:
        encrypted_data = file.read()

    if not encrypted_data:
        print("Error: The file is empty.")
        return

    for key in range(256):

        header = bytes(
            byte ^ key for byte in encrypted_data[:8]
        )

        for image_type, signature in SIGNATURES.items():

            if header.startswith(signature):
                print("Possible XOR key found:", key)
                print("Image format:", image_type)

                decrypted_data = bytes(
                    byte ^ key for byte in encrypted_data
                )

                directory = os.path.dirname(image_path)
                filename = os.path.basename(image_path)

                name, _ = os.path.splitext(filename)

                extension = ".png" if image_type == "PNG" else ".jpg"

                output_path = os.path.join(
                    directory,
                    "recovered_" + name + extension
                )

                with open(output_path, "wb") as file:
                    file.write(decrypted_data)

                print("Recovered image saved to:", output_path)
                return

    print("No matching JPEG or PNG signature found.")
    print("Check whether the file uses the expected XOR method.")


if __name__ == "__main__":
    image_path = input(
        "Enter encrypted image path: "
    ).strip().strip('"')

    if not os.path.isfile(image_path):
        print("Error: File not found.")
    else:
        brute_force_decrypt(image_path)