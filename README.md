# Numeric Methods

This repository contains Python scripts for numerical analysis, focused on iterative root-finding and fixed-point methods. It is built for a numeric analysis class and includes interactive examples that let you enter equations and see step-by-step convergence.

## Project Overview

- `punto_fijo.py`: Implements the fixed-point iteration method. It asks for a function `g(x)`, an initial guess `x0`, a tolerance, and a maximum number of iterations.
- `Secante.py`: Implements the secant method for solving equations of the form `f(x) = 0`.
- `utils.py`: Contains helper functions and a fixed-point iteration implementation that can be used as a library inside other scripts.

## How to Run

This project uses a Python virtual environment located in `.venv`.

From the project folder, run one of the scripts with the environment Python executable:

```powershell
.c/.venv/Scripts/python.exe punto_fijo.py
```

or

```powershell
.c/.venv/Scripts/python.exe Secante.py
```

If your terminal is already in the repository folder, the commands are:

```powershell
c:/Users/santi/OneDrive/Documentos/repos/numeric_methods/.venv/Scripts/python.exe punto_fijo.py
c:/Users/santi/OneDrive/Documentos/repos/numeric_methods/.venv/Scripts/python.exe Secante.py
```

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

## Requirements

- Python 3.14
- SymPy library

The virtual environment should already contain the required packages. If needed, install SymPy with:

```powershell
.c/.venv/Scripts/python.exe -m pip install sympy
```

## Notes

- The scripts are interactive and prompt you for input.
- The fixed-point method solves equations written as `x = g(x)`.
- The secant method solves equations written as `f(x) = 0`.

Good luck with your numeric analysis class!