import os
import re
import random

# Constants
INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"


def split_document(doc, target_slides):
    """
    Splits a markdown document into sections while ensuring the number of sections matches the target slides.

    Parameters:
    - doc (str): The markdown document as input.
    - target_slides (int): The desired number of slides.

    Returns:
    - list: A list of slide contents.
    """

    # Normalize whitespace
    doc = re.sub(r'\n\s*\n', '\n\n', doc.strip())

    # Try splitting by headers first (markdown `#` or `** bold **`)
    sections = re.split(r'\n(?=\*\*|\#)', doc)
    sections = [s.strip() for s in sections if s.strip()]

    # If no headers were found, split by paragraphs instead
    if len(sections) < 2:
        sections = re.split(r'\n\n+', doc)  # Split by double newlines

    # Ensure sections exist
    if not sections:
        return ["Slide 1: " + doc]  # Treat entire document as one slide

    # Adjust the number of sections to match the target slides
    while len(sections) < target_slides:
        # Split larger sections into smaller ones
        for i in range(len(sections)):
            if len(sections) < target_slides and len(sections[i]) > 50:  # Avoid splitting tiny sections
                midpoint = len(sections[i]) // 2
                split_index = sections[i].find(" ", midpoint)
                if split_index != -1:
                    sections.insert(i + 1, sections[i][split_index:].strip())
                    sections[i] = sections[i][:split_index].strip()

    while len(sections) > target_slides:
        # Merge shorter sections, ensuring index safety
        i = 0
        while len(sections) > target_slides and i < len(sections) - 1:
            sections[i] += "\n\n" + sections[i + 1]
            del sections[i + 1]
            i += 1  # Move forward to avoid skipping sections

    # Format slides
    slides = [f"Slide {i+1}: {sections[i]}" for i in range(len(sections))]

    return slides


def process_document(filename, target_slides):
    """
    Reads a markdown file, splits it into slides AFTER user input, and saves the output.

    Parameters:
    - filename (str): The markdown file name.
    - target_slides (int): Number of slides to generate.

    Returns:
    - None
    """
    filepath = os.path.join(INPUT_FOLDER, filename)
    if not os.path.exists(filepath):
        print(f"⚠️ Error: File '{filename}' not found.")
        return

    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()

    print(f"📖 Processing {filename} ({target_slides} slides)...")

    # **Perform splitting only after user provides a target slide number**
    slides = split_document(content, target_slides)

    # Save slides to output directory
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    output_file = os.path.join(OUTPUT_FOLDER, f"{os.path.splitext(filename)[0]}_slides.txt")
    with open(output_file, "w", encoding="utf-8") as out:
        out.write("\n\n--------------------------------------------------\n\n".join(slides))

    print(f"✅ Processed {filename} → {len(slides)} slides saved to {output_file}.\n")


def main():
    """
    Main function to process markdown files from input folder.
    User can specify slide count AFTER loading the file.
    """
    if not os.path.exists(INPUT_FOLDER):
        print(f"⚠️ Error: Input folder '{INPUT_FOLDER}' not found.")
        return

    files_to_process = [f for f in os.listdir(INPUT_FOLDER) if f.endswith(".md")]

    if not files_to_process:
        print("⚠️ No markdown files found in the input folder.")
        return

    for filename in files_to_process:
        while True:
            try:
                # Prompt user for number of slides, allowing Enter for random choice
                user_input = input(f"Slides for {filename} (3-50, press Enter for random): ").strip()

                if user_input == "":
                    target_slides = random.randint(3, 7)  # Randomize between 3-7
                    print(f"🎲 Randomly chosen {target_slides} slides for {filename}.")
                else:
                    target_slides = int(user_input)
                    if target_slides < 3 or target_slides > 50:
                        raise ValueError

                break  # Exit loop if input is valid
            except ValueError:
                print("⚠️ Invalid input. Please enter a number between 3 and 50.")

        # **Perform document splitting AFTER user selects slide count**
        process_document(filename, target_slides)

    print("🚀 Done!")


if __name__ == "__main__":
    main()
