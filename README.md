# study-notes-generator

Upload a PDF → get:
- Summary
- Flashcards
- Key terms
- Quiz questions


## Features

- PDF upload
- Automatic text extraction
- LLM-generated:
  - Summary
  - 10 flashcards
  - Key terms with definitions
  - 5 quiz questions
- Simple HTML/JS frontend


## Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/study-notes-tool.git
cd study-notes-tool/backend

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

OPENAI_API_KEY=your_api_key_here

uvicorn main:app --reload

cd frontend
# Option 1: simple static server
python -m http.server 5500

http://localhost:5500/index.html

MIT License

Copyright (c) 2026 Stephen Nganga

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



