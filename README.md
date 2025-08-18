# Task_Manager

A task manager project utizling data structures, and file I/O that I created to locally manage your daily tasks.

## Setup

1. **Get a Gemini API Key:**  
   Use the following link: [Google AI Studio](https://aistudio.google.com/app/apikey) and generate your own Gemini API key.

2. **Create the API Key File:**  
   In the root of this project (where you cloned/downloaded it), create a file named `my_api_key.env`.

3. **Input your API key to the .env file:**

   ```
   GEMINI_API_KEY=your-api-key-here
   ```

4. **Install dependencies:**  
   Python 3 duh.  
   Install required packages with:

   ```
   pip install google-genai
   pip install python-dotenv
   ```

5. **Run the program:**
   ```
   python task_manager.py
   ```
   or
   ```
   python3 task_manager.py
   ```

## Features

- Add, view, and delete tasks
- Tasks are stored locally in a CSV file
- Get AI suggestions for your tasks using Google's Gemini

---
