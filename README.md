# Module 11

---

## My DockerHub Image
[Visit the DockerHub Page](https://hub.docker.com/r/pruthvidholkia/is601_module11)


---

## Running Tests Locally

> Make sure your virtual environment is activated and dependencies installed.

### Install Dependencies

```bash```
pip install -r requirements.txt


---


## Clone the Repository

git clone https://github.com/pruthvidholkia/is601_module11_assignment.git

cd is601_module11_assignment


---


## Create & Activate Virtual Environment

python3 -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate


---


## Install Dependencies

pip install -r requirements.txt


---


## Run All Tests

pytest



## pytest

What it does: 

=> Runs all tests in your project:

Unit tests (e.g., test_calculator)

Integration tests (e.g., test_user, test_user_auth)

End‑to‑end tests (e.g., UI tests with Playwright)

=> Applies any pytest.ini settings and command line flags.

When to use: When you're doing a full verification before submission or after major changes.

