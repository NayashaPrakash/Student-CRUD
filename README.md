# Student Management API

A simple Flask-based REST API for managing students. Supports create, read, update, delete, and AI-generated profile summaries using Ollama.

---

## Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com/NayashaPrakash/Student-CRUD.git
```
Move to the project folder.

### 2. Create and activate virtual environment.
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3.  Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Ollama (Rrequired for summary generation)
Install Ollama: https://ollama.com

Pull and start the llama3 model:
```bash
ollama pull llama3.2
ollama serve
```

### 5. Start server
Start the Server
```bash
python app.py
```
The API will be available at:
http://localhost:5000

### 6. Test Endpoints.
All the endpints can be tested by running the test_students.sh file. Make it executable and then run it.
```bash
chmod +x test_students.sh
./test_students.sh
```

## Using the Hosted API
You can skip local setup and directly run API tests using the deployed version on Render.

### 1. Download the test_students_hosted.sh file.
### 2. Run the script.
```bash
chmod +x test_students_hosted.sh
./test_students_hosted.sh
```
Note: You need llama 3.2 model to run the summary endpoint. Check installation process in local setup.
