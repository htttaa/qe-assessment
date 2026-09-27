# QA Technical Assessment

## Overview

This repository contains my solution for the QA Technical Assessment, including automated tests for the **Create Task** and **Create Subtask** functionalities.

The automation was implemented using **Python, Pytest, and Playwright**, following a Page Object Model (POM) structure to improve maintainability and readability.

The test scenarios were designed based on the acceptance criteria provided in the assessment, with particular attention to functional requirements and boundary conditions.

---

## Technology Stack

* **Python**
* **Pytest**
* **Playwright**
* **Page Object Model (POM)**
* **HTML/CSS/JavaScript** — local application used as the test target

---

## Project Structure

```text
qe-assessment/
│
├── app/
│   └── index.html
│
├── pages/
│   └── tasks_page.py
│
├── test_data/
│   └── tasks.py
│
├── tests/
│   ├── conftest.py
│   ├── test_create_task.py
│   └── test_create_subtask.py
│
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

### Folder responsibilities

**`app/`**

Contains the local To-Do application used as the system under test.

**`pages/`**

Contains Page Object classes and locators used by the automated tests.

**`test_data/`**

Contains reusable test data, keeping test inputs separated from the test implementation.

**`tests/`**

Contains the automated test scenarios.

---

## Test Strategy

The automation focuses on the main acceptance criteria for task and subtask creation.

The scenarios were selected using a risk-based approach, prioritizing:

* Core business functionality
* Input validation
* Boundary conditions
* User interaction
* Successful data creation
* Feedback provided to the user

The tests also use **Boundary Value Analysis** for the Task Name field because the requirement defines a minimum of 3 and a maximum of 100 characters.

---

## Automated Scenarios

### 1. Create Task - Valid Data

**Test:** `test_user_can_create_a_task`

Validates that a logged-in user can create a task using valid information.

The test verifies that:

* The task can be created successfully.
* The task appears in the created tasks list.
* The task description is displayed.
* The success message is displayed.

---

### 2. Task Name - Boundary Value Analysis

**Test:** `test_task_name_boundary_values`

Validates the minimum and maximum boundaries defined for the Task Name field.

The following values are covered:

| Input          | Expected Result                           |
| -------------- | ----------------------------------------- |
| 2 characters   | Task should not be created                |
| 3 characters   | Task should be created                    |
| 100 characters | Task should be created                    |
| 101 characters | Browser should enforce the maximum length |

This scenario demonstrates how boundary values can be used to identify potential validation issues around input limits.

---

### 3. Create Subtask - Valid Data

**Test:** `test_user_can_create_a_subtask`

Validates the complete subtask creation flow.

The test verifies that:

* An existing task can be selected.
* The Create Subtasks modal is displayed.
* The task information is available in the modal.
* A subtask can be created with valid information.
* The subtask is added to the list.
* The subtask counter is updated.
* The success message is displayed.

---

## Page Object Model

The project uses the **Page Object Model** to separate test logic from UI locators and interactions.

For example, instead of placing selectors directly inside every test, the `TasksPage` class provides reusable methods such as:

```python
tasks_page.create_task(...)
tasks_page.open_subtask_modal(...)
tasks_page.create_subtask(...)
```

This approach makes the tests easier to read and reduces duplication.

If the UI selectors change in the future, the main changes can be concentrated in the Page Object instead of being repeated across multiple test cases.

---

## Test Data

Test data is stored separately in:

```text
test_data/tasks.py
```

Example:

```python
VALID_TASK = {
    "name": "Prepare QA Assessment",
    "description": "Complete the QA technical assessment.",
}
```

Keeping test data separate makes it easier to maintain and extend the test suite.

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd qe-assessment
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Install Playwright browsers

```powershell
python -m playwright install
```

---

## Running the Application

Start the local application with:

```powershell
python -m http.server 8000 --directory app
```

The application will be available at:

```text
http://localhost:8000
```

Keep this terminal running while executing the tests.

---

## Running the Tests

Open another terminal, activate the virtual environment, and run:

```powershell
python -m pytest
```

To run a specific test file:

```powershell
python -m pytest tests/test_create_task.py
```

or:

```powershell
python -m pytest tests/test_create_subtask.py
```

---

## Expected Result

A successful execution should report all automated scenarios as passed:

```text
3 passed
```

---

## Assumptions and Scope

The assessment did not provide a production application URL or repository. Therefore, a local implementation of the To-Do application was used as the system under test.

The local application was created specifically to reproduce the requirements needed for the automated scenarios.

The current automation scope focuses on the **Create Task** and **Create Subtask** requirements requested for the automation exercise.

Features such as reminders, task completion status, near-due-date colors, and other acceptance criteria outside the implemented automation scope were not included in the automated suite.

---

## Future Improvements

If this were a production project, I would consider expanding the automation suite with:

* API-level testing
* Negative scenarios for subtask validation
* Task description boundary testing
* Due date validation
* Urgent task validation
* Enter key submission
* Reminder functionality
* Task completion and deadline behavior
* Cross-browser execution
* Mobile/responsive testing
* Accessibility checks
* CI/CD integration
* Test reporting and artifacts
* Parallel test execution

The automation strategy would continue to prioritize stable, business-critical and frequently executed scenarios while keeping exploratory and highly dynamic scenarios suitable for manual testing.

---

## QA Approach

The overall approach was based on:

1. Understanding the acceptance criteria.
2. Identifying the main functional flows.
3. Identifying validation rules and boundaries.
4. Selecting high-value scenarios for automation.
5. Separating test logic, page interactions, and test data.
6. Implementing reusable Page Objects.
7. Executing the tests and analyzing failures.
8. Adjusting assertions based on the actual application behavior.
9. Keeping the automation maintainable and extensible.

This approach aims to provide reliable automated feedback while keeping the test suite readable and maintainable.
