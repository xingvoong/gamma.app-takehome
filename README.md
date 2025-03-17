# gamma.app takehome

## 🚀 Overview
This project showcases my problem-solving skills in prompt engineering and coding by converting markdown documents into structured slide sections. It dynamically processes documents based on user input and ensures the generated slides match the target number of slides while preserving all content.


## 🎯 Problem-Solving/Coding Approach

- **Define scope and constraints:** Ensures that document parsing and slide formatting aligned with user-defined constraints.
- **Divide and conquer:** Break down the problem into two or more smaller similar problems. For example, to split a document by headers, if no headers were found, split by paragraphs instead.
- **Agile methodology** is used for this coding project which focuses on incremental and iterative development.
- **Efficient Text Processing:** Use **regex-based sectioning** while handling **edge cases** (e.g., missing headers).
- **Dynamic Slide Allocation:** Balance sections by **splitting and merging content** based on user input.
- **Error Handling & Debugging:** Address inconsistencies in input formats and provided clear user prompts.

---

## 🤖 Prompt Engineering insights/process:
Since a goal of this homework is to show off my prompt engineering skills, I want to go ahead and explain my prompting process.
- First I want the LLM model to understand the instruction clearly by feeding in **The Requirements** given by Gamma in the takehome.
- I then provide reference and context text by giving the text in **The Task** section provided by Gamma
In the third step, I give the text example doc to the LLM model.

These first three steps provide me with a prototype solution that I can iterate on. To improve the solution I have, I do the following:

**1: Give the LLM model more time to think** by writing "Take your time and work on your solution and reasoning before answering me"

**2: Break down the tasks into subtasks:**
Here is the breakdown

-   **Understanding Document Structure**

    -   Identified headings (`#`, `##`) and bold text (`**`) as primary section markers.
    -   Used paragraph breaks when no clear markers existed.
-   **Content Preservation & Splitting**

    -   Ensured the entire document was retained, maintaining logical flow.
    -   Split long sections when slides were too few, and merged adjacent ones when too many.
-   **Adaptive Slide Targeting**

    -   Dynamically adjusted slide count based on user input.
    -   Used natural breakpoints (sentences, paragraphs) to avoid abrupt truncation.
-   **Refinement & Testing**

    -   Iteratively tested with different markdown structures.
    -   Ensured proper handling of lists, formatting, and spacing for readability.

**3: Give more examples, aka a few shot learning**

I provided a few examples from markdown files I wrote and how I want them to be splitted. This shows the model that I look for in terms of output and structures.

The examples I use can be found in *input* folder. The logic of how I want the documents to be splitted can be found in the code and comments of gamma.py.

## ✅ Requirements Fulfilled
This program meets the following requirements:
- **Takes as input**:
  - A **document**, as a string in **Markdown format**.
  - A **target number of slides**, as an integer between **1 and 50**.
- **Outputs**:
  - An **array of document sections** in **plain text format**.
  - A `.txt` file containing structured slides in the `output/` folder.
- **Preserves content integrity**:
  - If the output sections are joined back together, they exactly match the original document.

---

## 🔥 Features
- ✅ **Parses Markdown Documents** → Automatically detects headers and bullet points.
- 🎯 **User-Defined Slide Count** → Allows users to specify the target number of slides.
- 📂 **Batch Processing** → Processes multiple markdown files from the `input/` folder.
- 📄 **Plain Text Slide Output** → Saves slides as text files inside `output/` (ignored in `.gitignore`).
- 🔥 **Content Integrity** → Ensures all document content is preserved.
- 🛠️ **Error Handling** → Adjusts output for documents with missing headers and provides warnings.

---

## 🔧 How It Works

### **1️⃣ Input:**
- The program scans the `input/` folder for `.md` files.
- The user is prompted to choose the number of slides per file.

### **2️⃣ Processing:**
- Extracts sections using **headers** (`#` or `**bold**` format) and **bullet points**.
- If there are fewer sections than the target slides → splits longer sections.
- If there are more sections than the target slides → merges smaller sections.
- Ensures the entire content is maintained while keeping sections balanced.

### **3️⃣ Output:**
- The formatted slides are saved as `.txt` files inside the `output/` directory.
- The script **returns an array of slides in plain text format** for further processing.

---

## 📥 Installation & Usage

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/xingvoong/gamma.app-takehome
cd gamma.app-takehome
```

### **2️⃣ Install Dependencies**
> *(This script runs on Python 3 and requires no external dependencies.)*

### **3️⃣ Run the Program**
```bash
python3 gamma.py
```
- Place **Markdown files** inside the `input/` folder.
- Follow the prompts to set the **number of slides per file**.

---

## 📂 File Structure

```
/gamma.app-takehome
│── input/              # Folder containing markdown documents
│── output/             # Folder where slide text files are saved (ignored in .gitignore)
│── gamma.py            # Main Python script
│── .gitignore          # Ignores system files and output folder
│── README.md           # Project documentation
```

---


🎉 **Ready to turn long documents into concise, structured slides?** Run the script and generate your own slides now! Please reach out to me at xingvoong@gmail.com if you have any trouble running the code🚀