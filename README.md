# QAAgent-Task-Shreyas-Saraf
🚀 QAgenie - AI-Powered Frontend Test Automation for Recruter.ai
QAgenie is an intelligent, AI-powered Quality Assurance assistant that automates end-to-end frontend test case generation, execution, and reporting for Recruter.ai.

It analyzes "How-to" videos, understands user flows, and automatically builds reliable Playwright tests—making your testing process faster, more thorough, and error-free.

🎯 Key Features

✅ AI Test Case Generator

Extracts transcripts from Recruter.ai tutorial YouTube videos

Uses Google Gemini AI to generate structured frontend test cases

Covers core user flows, edge cases, cross-browser tests, accessibility, and mobile variants


✅ Automated Test Script Creation & Execution

Converts AI-generated test cases into Playwright scripts

Runs tests across multiple browsers (Chromium, Firefox, Webkit)

Tests responsive behavior on mobile viewports (iPhone, Pixel)

Captures screenshots, videos, and detailed logs


✅ Comprehensive Reporting

Saves results in JSON, Markdown, and PDF formats

Generates easy-to-read dashboards using Streamlit

Optionally emails test reports to the QA team



📦 Tech Stack Used
YouTube Transcript API

Google Gemini AI

LangChain + ChromaDB

Playwright for automated browser testing

Streamlit for result dashboards

Pandas, pdfkit for reporting



🔧 How It Works
Video Understanding

Fetches the transcript of the provided Recruter.ai YouTube video

Optionally uses Whisper for transcription


Test Case Generation (AI)

Sends transcript to Gemini AI with detailed prompts

AI returns structured, ready-to-use test cases


Automated Script Creation

Converts test cases into Playwright-compatible scripts

Includes multi-browser and mobile responsiveness checks


Test Execution

Runs tests locally or against Recruter.ai staging environment

Captures screenshots, videos, and logs


Result Reporting

Saves results as JSON, Markdown, PDF

Displays interactive dashboard via Streamlit

Optionally emails reports to configured recipients


🚀 Quick Start
1. Install Dependencies
bash
Copy
Edit
pip install youtube-transcript-api langchain-community chromadb pydantic playwright google-generativeai==0.3.2 streamlit pandas pdfkit  
playwright install
2. Set Your Config
Update Config in the code:

YOUTUBE_URL → Your Recruter.ai tutorial video link

GEMINI_API_KEY → Your Google Gemini API Key

EMAIL_CONFIG → Email setup for report sending

3. Run the QA Pipeline
bash
Copy
Edit
python your_script_name.py
4. View Dashboard
bash
Copy
Edit
streamlit run your_script_name.py
📂 Project Structure
File/Folder	Purpose
test_cases.json	AI-generated test cases (JSON)
test_cases.md	Human-readable test cases (Markdown)
test_script.spec.ts	Playwright test script (Auto-generated)
test_results/	Test results, screenshots, videos, reports

⚡ Example Output
✅ Playwright runs across Chrome, Firefox, Webkit
✅ Tests UI, responsiveness, error handling
✅ Screenshots and videos captured for each failure
✅ Dashboard shows total tests, passed/failed count
✅ Reports emailed to your QA team

🎨 Future Enhancements
Whisper-based audio transcription option

Gherkin syntax test case output

LM Studio local LLM integration

More advanced error reporting

🤖 About QAgenie
QAgenie is your calm, thorough AI QA assistant, designed to:
✅ Understand user journeys from videos and documents
✅ Generate precise, reliable test cases
✅ Run automated frontend tests systematically
✅ Provide clear, actionable reports

Mission: "Ensure flawless user experiences on Recruter.ai."

🛠 Requirements
Python 3.8+

Playwright installed

Google Gemini API access

Contributions Welcome – Let's make testing smarter! 🚀
