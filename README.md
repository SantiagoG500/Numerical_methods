    ---
title: Numerical Methods Calculator
colorFrom: blue
colorTo: indigo
sdk: gradio
python_version: "3.10"
sdk_version: 5.0.1
app_file: app.py
pinned: false
---



# Numeric Methods

This repository contains Python scripts for numerical analysis, focused on iterative root-finding and fixed-point methods. It is built for a numeric analysis class and includes interactive examples that let you enter equations and see step-by-step convergence.

## Project Members

- Esteban Bejarano
- Santiago Gamboa
- Victor Molina

## Project Overview

- `punto_fijo.py`: Implements the fixed-point iteration method. It asks for a function `g(x)`, an initial guess `x0`, a tolerance, and a maximum number of iterations.
- `Secante.py`: Implements the secant method for solving equations of the form `f(x) = 0`.
- `utils.py`: Contains helper functions and a fixed-point iteration implementation that can be used as a library inside other scripts.

### Prerequisites

* **Python 3.9** or higher.
* **pip** (Python package installer).

## How to Run

Follow these instructions to get a copy of the project up and running on your local machine.

### Installation & Setup

1. **Clone the repository:**

    ```bash
    git clone [https://github.com/your-username/numeric_methods.git](https://github.com/your-username/numeric_methods.git)
    cd numeric_methods
    ```

2. **Create a virtual environment:**

* **Windows:**
    ```powershell
        python -m venv .venv
    ```

* **macOS/Linux:**
    ```bash
    python3 -m venv .venv
    ```


3. **Activate the environment:**
* **Windows (PowerShell):**
    ```powershell
    .\.venv\Scripts\Activate.ps1
    ```

* **macOS/Linux:**
    ```bash
    source .venv/bin/activate
    ```

4. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```



## Usage

Once the dependencies are installed, you can launch the interactive interface by running:

```bash
python app.py
```

After running the command, open your browser and navigate to the local URL provided in the terminal (usually `http://127.0.0.1:7860`).


## Example Inputs

For `punto_fijo.py`:
- Function: `cos(x)`
- Initial guess: `0`
- Tolerance: `1e-6`
- Max iterations: `100`

For `Secante.py`:
- Function: `x**2 - 2`
- First guess: `1`
- Second guess: `2`
- Relative error: `1e-6`
- Max iterations: `100`


## Notes

- The scripts are interactive and prompt you for input.
- The fixed-point method solves equations written as `x = g(x)`.
- The secant method solves equations written as `f(x) = 0`.

Good luck with your numeric analysis class!
