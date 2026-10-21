# Build It progress

Practice code written from scratch, one step at a time (see the `build-it-tutor` skill).

## Lesson 4: Calculus for ML (`lesson04_calculus.py`)

| Step | Topic | Status | Notes |
|------|-------|--------|-------|
| 1 | Numerical derivative | Done | One-sided vs two-sided; two-sided error ~1e-12 vs h for one-sided |
| 2 | Partial derivatives and gradients | Done | Gradient of x² + 3xy + y² at (1, 2) = (8, 7) |
| 3 | Gradient descent on x² | Done | Used x² + x; found bottom at x = −0.5. lr test: 0.1 slow, 0.5 one jump, 1.0 bounces, 1.1 explodes |
| 4 | Gradient descent in 2D | Done | Bowl → straight line to (0, 0); f2 = x² + 3xy + y² slides down y = −x forever (saddle, no bottom) |
| 5 | Numerical vs analytical table | Next | Task given 2026-10-21: `import math`, 5 function/derivative pairs at x = 2, `tests` list, formatted table; bonus: error vs h |
| 6 | Numerical Hessian | | |
| 7 | Taylor approximation | | |
| 8 | Linear regression training loop | | |
| Ex 1–3 | Exercises (2nd derivative, 2D descent, momentum) | | |

## Python learned so far
Variables, `print`, `def`/`return`, passing a function as an input, `for` loops,
`range` (stops before the end), lists vs tuples, the order of `/` and `*`,
reading tracebacks, scientific notation, updating a variable from its old value,
nested loops, f-strings, unpacking (`a, b = pair`), returning two values,
`%` and `if`, why tuples don't do vector math (`3 * (8, 6)` repeats).
