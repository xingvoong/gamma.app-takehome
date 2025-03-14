import re

def split_document(doc, target_slides):
    """
    Split a markdown document into sections based on its headings and bullet points,
    and organize them into slides to match the target number of slides.

    Parameters:
    doc (str): The markdown document as input.
    target_slides (int): The desired number of slides.

    Returns:
    list: A list of text sections (as strings) that fit the target slides.
    """
    # Normalize line breaks and remove excess spaces
    doc = re.sub(r'\n\s*\n', '\n\n', doc.strip())

    # Split document into sections based on headers
    sections = re.split(r'\n(?=\*\*|\#)', doc)
    sections = [s.strip() for s in sections if s.strip()]

    # If there are fewer sections than the target slides, adjust accordingly
    while len(sections) < target_slides:
        for i in range(len(sections)):
            if len(sections) < target_slides:
                midpoint = len(sections[i]) // 2
                split_index = sections[i].find(" ", midpoint)  # Find a reasonable split point
                if split_index != -1:
                    sections.insert(i + 1, sections[i][split_index:].strip())
                    sections[i] = sections[i][:split_index].strip()

    # If we have more sections than slides, merge sections
    while len(sections) > target_slides:
        for i in range(len(sections) - 1):
            if len(sections) > target_slides:
                sections[i] += "\n\n" + sections.pop(i + 1)

    # Format the output into slides
    slides = [f"Slide {i+1}: {sections[i]}" for i in range(len(sections))]

    return slides


# Example Document 1 (doc1)
doc1 = """
# Generative AI is a transformative technology

The last year has seen a spectacular acceleration in generative AI: systems able to generate text / image conditioned on text and images. Those systems can help humans:

- produce superb creative content (text, code, graphics)
- read, process and summarise unstructured content streams thousands of times faster than humans
- interact with the world (exposed through natural or application interfaces) to execute workflows faster than ever before.

The power of generative AI was suddenly demonstrated to the general audience with the release of ChatGPT; this kind of product has been in the making by only a few small teams across the world — the few researchers of these teams are now the limiting factor to create new economic actors in the field.

Generative AI is about to boost productivity in all sectors and create a new industry (10B market size as of 2022, projected to be 110B by 2030, with an estimated growth rate of 35% per year), by seamlessly enhancing the human mind with machine capabilities.

# An oligopoly is shaping up

Generative AI technologies are based on years of research made in many parts of the industry and academia. The final breakthroughs, i.e. scaling training to internet-wide data and aligning models with human feedback, finally made these technologies usable by many; these breakthroughs were made by very few actors, the largest of which (OpenAI) appears to have hegemonic intention over the market.

These very few actors train generative models and hold them as assets; they serve it to thousands of third-party productivity enhancing products, in addition to also serving first-party chatbot-like products.

## We believe that most of the value in the emerging generative AI market will be located in the hard-to-make technology, i.e. the generative models themselves.

Those models need to be trained on thousands of very powerful machines, on trillions of words coming from high-quality sources, which is one factor that sets a high barrier to entry. The second important barrier lies in the difficulty to assemble an experienced team, something that mistral.ai will be in a unique position of doing.
"""

# Set target number of slides
target_slides = 3

# Call the function to split the document into the required number of slides
result = split_document(doc1, target_slides)

# Print the result
for slide in result:
    print(slide)
    print("\n" + "-"*50 + "\n")  # Just to separate slides visually
