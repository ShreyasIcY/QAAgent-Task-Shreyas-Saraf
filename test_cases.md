# QAgenie Test Suite

*Ensure flawless user experiences on Recruter.ai*
*Generated on: 2025-07-06 21:09*

## Create Interview with Existing Job Description
**Purpose**: Verify the creation of an interview using a pre-existing job description.

- **Category**: functional
- **Priority**: high
- **Approach**: Systematic validation

1. **Paste a valid job description into the provided field.**
   → Expected: Job description is accepted and displayed correctly.
   → Element: `#job-description-input`
2. **Click the 'Create Interview' button.**
   → Expected: Interview is created successfully, and a unique interview link is displayed.
   → Element: `#create-interview-button`

---
## Create Interview using Enhanced JD Feature
**Purpose**: Verify the creation of an interview using the enhanced JD feature with a job title.

- **Category**: functional
- **Priority**: high
- **Approach**: Systematic validation

1. **Enter a job title (e.g., 'JavaScript Developer') into the enhanced JD field.**
   → Expected: The AI generates a job description based on the provided job title.
   → Element: `#enhanced-jd-input`
2. **Click the 'Create Interview' button.**
   → Expected: Interview is created successfully using the AI-generated job description.
   → Element: `#create-interview-button`

---
## Customize Interview Questions
**Purpose**: Verify the ability to customize the AI-suggested interview questions.

- **Category**: functional
- **Priority**: medium
- **Approach**: Systematic validation

1. **Review the AI-suggested questions.**
   → Expected: AI suggests standard and role-based questions based on the job description.
   → Element: `.suggested-questions`
2. **Edit an existing question and add a new question.**
   → Expected: Changes are saved, and the updated questions are reflected.
   → Element: `.question-editor`

---
## Select AI Avatar (Advanced Plan)
**Purpose**: Verify the functionality to select an AI avatar for advanced plan users.

- **Category**: functional
- **Priority**: medium
- **Approach**: Systematic validation

1. **Navigate to the AI avatar selection section.**
   → Expected: Avatar selection options are displayed.
   → Element: `#ai-avatar-selector`
2. **Select an AI avatar.**
   → Expected: Selected avatar is applied and confirmed.
   → Element: `.avatar-option`

---
## Handle Empty Job Description Input
**Purpose**: Verify system behavior when creating an interview with an empty job description.

- **Category**: functional
- **Priority**: high
- **Approach**: Systematic validation

1. **Leave the job description field empty and click 'Create Interview'.**
   → Expected: An appropriate error message is displayed indicating the required field.
   → Element: `#job-description-input`
2. **Enter a job description and click 'Create Interview'.**
   → Expected: Interview is created successfully.
   → Element: `#create-interview-button`

---
## Remove and Reorder Questions
**Purpose**: Verify the ability to remove and reorder interview questions.

- **Category**: functional
- **Priority**: medium
- **Approach**: Systematic validation

1. **Select a question and click the 'Remove' button.**
   → Expected: The selected question is removed from the list.
   → Element: `.remove-question-button`
2. **Drag and drop questions to reorder them.**
   → Expected: The order of questions is updated accordingly.
   → Element: `.question-item`

---
