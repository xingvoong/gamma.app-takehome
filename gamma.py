import os
import re
import random

def split_document(doc, target_slides):
    """
    Splits a markdown document into sections while ensuring the number of sections matches the target slides.

    Parameters:
    - doc (str): The markdown document as input.
    - target_slides (int): The desired number of slides.

    Returns:
    - list: A list of text sections (each section corresponds to one slide).
    """

    # Normalize whitespace
    doc = re.sub(r'\n\s*\n', '\n\n', doc.strip())

    # Try splitting by headers first (Markdown # headers or bold **text**)
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
        for i in range(len(sections)):
            if len(sections) < target_slides and len(sections[i]) > 50:  # Avoid splitting small sections
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

    return sections  # ✅ Returns an array of document sections in plain text format


def process_document(filename, target_slides):
    """
    Reads a markdown file, splits it into slides, saves the output to a text file, and returns the slides.

    Parameters:
    - filename (str): Path to the markdown file.
    - target_slides (int): Number of slides to split into.

    Returns:
    - list: Array of document sections in plain text format.
    """
    print(f"📖 Processing {filename} ({target_slides} slides)...")

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    slides = split_document(content, target_slides)

    # Ensure output folder exists
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    # Save output slides to a .txt file
    output_filename = os.path.join(output_folder, os.path.basename(filename).replace(".md", ".txt"))
    with open(output_filename, "w", encoding="utf-8") as output_file:
        for i, slide in enumerate(slides):
            output_file.write(f"Slide {i + 1}:\n{slide}\n")
            output_file.write("-" * 50 + "\n")

    print(f"✅ Processed {filename} → {len(slides)} slides saved to {output_filename}")

    return slides  # Returns the slides as a list


def main():
    """
    Main function to process all markdown files in the "input" folder.
    Allows the user to choose the number of slides for each document.
    """
    input_folder = "input"
    if not os.path.exists(input_folder):
        print(f"❌ Error: Folder '{input_folder}' not found.")
        return

    files_to_process = [f for f in os.listdir(input_folder) if f.endswith(".md")]

    if not files_to_process:
        print("❌ No Markdown files found in the 'input' folder.")
        return

    for filename in files_to_process:
        filepath = os.path.join(input_folder, filename)

        # Let the user choose the number of slides
        while True:
            try:
                target_slides = input(f"Slides for {filename} (3-50, press Enter for random): ")
                if target_slides.strip() == "":
                    target_slides = random.randint(3, 7)  # Random between 3-7
                else:
                    target_slides = int(target_slides)

                if 3 <= target_slides <= 50:
                    break
                else:
                    print("⚠️ Invalid input. Please enter a number between 3 and 50.")
            except ValueError:
                print("⚠️ Invalid input. Please enter a valid number.")

        process_document(filepath, target_slides)

    print("🚀 Done!")


if __name__ == "__main__":
    main()
