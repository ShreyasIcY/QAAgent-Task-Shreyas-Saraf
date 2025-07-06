# report.py
import streamlit as st
import json
from pathlib import Path
from datetime import datetime

# Config
TEST_CASES_FILE = "test_cases.json"
RESULTS_DIR = "test_results"

# UI Setup
st.set_page_config(layout="wide", page_title="Recruter.ai QA Dashboard")
st.title("🎯 QA Test Automation Dashboard")
st.write(f"Last run: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Load Data
@st.cache_data
def load_data():
    test_cases = json.load(open(TEST_CASES_FILE)) if Path(TEST_CASES_FILE).exists() else []
    results = {"summary": {"total": 0, "passed": 0, "failed": 0}}
    
    try:
        results = json.load(open(f"{RESULTS_DIR}/test-results.json"))
    except:
        pass
        
    return test_cases, results

test_cases, results = load_data()

# Dashboard Sections
col1, col2, col3 = st.columns(3)
col1.metric("Total Test Cases", len(test_cases))
col2.metric("Passed Tests", results["summary"]["passed"])
col3.metric("Failed Tests", results["summary"]["failed"])

# Test Case Explorer
st.header("📋 Test Cases")
for tc in test_cases:
    with st.expander(f"{tc['title']} ({tc['priority']})"):
        st.write(f"**Description**: {tc['description']}")
        st.write(f"**Category**: {tc['category']}")
        
        for step in tc["steps"]:
            st.markdown(f"""
            **{step['step_number']}. {step['action']}**  
            → *Expected*: {step['expected_result']}
            """)

# Test Results
st.header("🔍 Execution Results")
if "suites" in results:
    for suite in results["suites"]:
        for test in suite["tests"]:
            status = "✅ PASS" if test["status"] == "passed" else "❌ FAIL"
            st.markdown(f"""
            **{test['title']}**  
            **Status**: {status} | **Duration**: {test['duration']}ms
            """)
            
            if test["status"] == "failed":
                st.error(test.get("error", {}).get("message", "No error details"))
else:
    st.warning("No test results found")

# Sidebar Controls
with st.sidebar:
    st.header("Controls")
    if st.button("🔄 Refresh Data"):
        st.cache_data.clear()
        st.rerun()
    
    st.download_button(
        "📥 Download Results",
        data=json.dumps({"test_cases": test_cases, "results": results}),
        file_name="qa_results.json"
    )