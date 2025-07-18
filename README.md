# Module 10

---

## My DockerHub Image
[Visit the DockerHub Page](https://hub.docker.com/r/pruthvidholkia/is601_module10)


---


## pytest -s -v tests/integration/test_user.py --preserve-db

What it does:

Runs only the test_user.py integration tests.
-s: Shows print/log output in real time.
-v: Provides verbose test info (test names, statuses).
--preserve-db: Tells conftest.py not to drop or truncate the test database after tests—so you can inspect the data afterwards.

When to use: When debugging a specific test and you want the DB state preserved for manual review.



## pytest -s -v tests/integration/test_user.py

=> What it does: Same as above, but without --preserve-db. That means the test database will be cleaned up after tests complete.
=> When to use: When rerunning integration tests in their default clean environment, and you don’t need to inspect the DB afterward.


## pytest

What it does: 
=> Runs all tests in your project:

Unit tests (e.g., test_calculator)
Integration tests (e.g., test_user, test_user_auth)
End‑to‑end tests (e.g., UI tests with Playwright)

=> Applies any pytest.ini settings and command line flags.
When to use: When you're doing a full verification before submission or after major changes.


---

## Github Action workflow
![Github action](/screenshots/github_action.png)


---


## GitHub Actions Workflow Screenshot
![GitHub Actions Workflow](/screenshots/docker_push.png)  
[This screenshot shows the passing CI pipeline with 100% test coverage.]
