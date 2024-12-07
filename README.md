# poetryPlaywright

Python Playwright Project for E2E tests and web scraping with Devcontainer.

## Overview

This project is a template for the modern web scraping and E2E testing with Playwright. It uses the Playwright library to interact with the browser and the web page. The project is set up with a Devcontainer for a consistent development environment.

### Package Manager:

- poetry

### Linter and Formatter:

- mypy
- flake8
- black
- isort

All of linters and formatters are controlled by `pysen`.

### Pre-installed:

- python
- poetry
- python-dotenv
- playwright
- beautifulsoup4
- requests

## How to use

### Initial Setup

1. Clone this repository.
2. Open the project in VSCode.
3. Press `F1` and select `Dev-Containers: Reopen in Container`.
4. (poetry install is automatically executed)
5. Open the terminal and run the following command:
6. Install the required browser driver.

```bash
# all
poetry run playwright install

# specific
poetry run playwright install [chromium|firefox|webkit]
```

NOTE: additional information can be found in the [Playwright documentation](https://playwright.dev/python/docs/intro).

### Run the code

#### Scraping

```bash
poetry run python src/example.py
```

#### E2E Testing

```bash
poetry run pytest tests/test_example.py
```
