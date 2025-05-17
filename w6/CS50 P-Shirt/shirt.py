import sys
from PIL import Image, ImageOps


def main():
    # Validate command-line arguments and get input/output filenames
    input, output = validate_args()
    apply_shirt(input, output)


def apply_shirt(input, output):
    # Open the input image and convert to RGBA for transparency support
    input_image = Image.open(input).convert("RGBA")
    # Open the shirt overlay image (must be PNG with transparency)
    shirt_image = Image.open("shirt.png").convert("RGBA")

    # Resize and crop input image to match shirt size
    input_img_resized = ImageOps.fit(input_image, shirt_image.size)
    # Overlay the shirt image using its alpha channel as mask
    input_img_resized.paste(shirt_image, (0, 0), shirt_image)

    # Convert to RGB if saving as JPEG (JPEG does not support transparency)
    if output.lower().endswith((".jpg", ".jpeg")):
        input_img_resized = input_img_resized.convert("RGB")
    # Save the final image
    input_img_resized.save(output)


def validate_args():
    # Check for correct number of command-line arguments
    if len(sys.argv) == 3:
        pass
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

    # Check if input file exists
    try:
        with open(sys.argv[1]) as file:
            pass
    except FileNotFoundError:
        sys.exit("Input does not exist")

    # Validate file extensions
    valid_extensions = [".jpg", ".jpeg", ".png"]
    input = sys.argv[1].lower()
    output = sys.argv[2].lower()

    # Check if input and output have valid extensions
    if not input.endswith(tuple(valid_extensions)):
        sys.exit("Invalid input")
    elif not output.endswith(tuple(valid_extensions)):
        sys.exit("Invalid output")

    # Check if input and output extensions match
    input_extension = input.split(".")[-1]
    output_extension = output.split(".")[-1]

    if input_extension != output_extension:
        sys.exit("Input and output have different extensions")

    return input, output


if __name__ == "__main__":
    main()