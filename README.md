# Python Starter Project
A simple starter project for Python projects:

- Simple Package/Module structure
- Testing with [pytest](https://docs.pytest.org/en/stable/)
- Linting with [autopep8](https://pypi.org/project/autopep8/)
- CI with [Github Actions](https://docs.github.com/en/actions/quickstart)

## Installation
1. Clone the repository
2. [Create a virtual environment](#setting-up-a-virthual-environment-with-mini-conda) [optional]
3. Install the requirements
    ```bash
    pip install -r requirements.txt
    ```
4. Run the project
    ```bash
    python main.py
    ```

## Setting up a virtual environment with mini conda
1. [Install mini conda](https://docs.conda.io/en/latest/miniconda.html)
2. Create a virtual environment
    ```bash
    conda create -n <env_name> python=3.8
    ```
3. Activate the virtual environment
    ```bash
    conda activate <env_name>
    ```

## Run tests
In root of project run:
```bash
pytest
```

## Run linting
```bash
autopep8 --in-place --recursive .
```

