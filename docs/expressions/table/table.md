---
title: table
sidebar_label: table
---

# table

Creates a data table that evaluates mathematical formulas over a range of input values, displaying computed results in a labeled grid.

**Utility:** Create a data table evaluating formulas over a range of values

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `position` | `at(row, col)` | Yes | Position on canvas using logical row, col coordinates |
| `formulas` | `string (one or more)` | Yes | Column formulas as quoted strings - e.g., "x", "x^2", "sin(x)". Can also pass def() variable references. |
| `range` | `range(start, end) \| range(start, end, step) \| range(v1, v2, ...)` | Yes | Values to evaluate: range(0, 5) for 0 to 5, range(0, 10, 2) for step of 2, or range(0.5, 0.9, 0.99) for explicit values |
| `header` | `header("label1", "label2", ...)` | No | Custom column headers as quoted strings. If omitted, formula strings are used as headers. |
| `color` | `c(colorName)` | No | Table color - e.g., c(blue), c(red), c(green) |
| `fontSize` | `f(size)` | No | Font size for table cells - e.g., f(16) |
| `type` | `type(n)` | No | Render mode variant |

## Variants

### Basic two-column table with range

```
T = table(at(row, col), "x", "x^2", range(0, 5))
```

Table with x values from 0 to 5, computing x^2

### Multi-column table with step

```
T = table(at(row, col), "x", "x^2", "2*x", range(0, 5, 1))
```

Three-column table: x, x^2, and 2*x with step size 1

### Table with explicit values

```
T = table(at(row, col), "x", "(x-1)/(x^2-1)", range(0.5, 0.9, 0.99, 0.999, 1.001, 1.01, 1.1, 2))
```

Table with hand-picked x-values, useful for limit exploration

### Table with def() function references

```
eq = def(x, "x^2")
T = table(at(row, col), "x", eq, range(0, 5))
```

Column uses a previously defined function variable

### Table with custom headers

```
T = table(at(row, col), header("n", "n^2", "\\sin(n)"), "n", "n^2", "sin(n)", range(1, 10))
```

Custom LaTeX headers separate from formula definitions

### Colored table

```
T = table(at(row, col), "x", "x^2", range(0, 5), c(blue))
```

Table with blue color styling

### Table with font size

```
T = table(at(row, col), "x", "formula", range(0, 5), f(16))
```

Table with custom font size

## Examples

### Derivative comparison table - show f(x) and f'(x) side by side, plot both

```
T = table(at(6, 2), "x", "x^2", "2*x", range(0, 5, 1))
G1 = g2d(at(1, 14), 12, 18, range(-1, 5, 1), range(-1, 15, 2))
plottable(G1, T, 2, c(blue))
G2 = g2d(at(15, 14), 12, 18, range(-1, 5, 1), range(-2, 12, 2))
plottable(G2, T, 3, c(red))
```

### Limit exploration table - values approaching x=1 from both sides

```
eq = def(x, "x^2")
slopeeq = def(x, "(x^2-1)/(x-1)")
t = table(at(1, 7), "x", eq, slopeeq, range(2, 1.5, 1.1, 1.01, 1.001), c(blue))
t = table(at(15, 7), "x", eq, slopeeq, range(0, 0.5, 0.9, 0.99, 0.999), c(green))
```

### Table with graph plot using plottable

```
table_1 = table(at(4, 26), "x", "(x-1)/(x^2-1)", range(0, 0.2, 0.5, 0.7, 0.8, 0.9, 0.99, 0.999, 1, 1.1, 1.2, 2), f(16))
graph_1 = g2d(at(4.2, 37), 16.6, 16.1, range(-1, 2, 0.5), range(-1, 2, 0.5), grid())
plot_1 = plottable(graph_1, table_1, 2)
```

### Simple table for arrow annotation

```
T = table(at(2, 30), "x", "y = x", range(1, 3))
arrow(at(T, 1, 2), P, "f(x)")
```

### Table with tangent line visualization

```
eq = def(x, "x^2")
slopeeq = def(x, "(x^2-1)/(x-1)")
G = g2d(at(2, 3), 30, 30, range(-2, 3), range(-1, 5))
pl1 = plot(G, eq)
t = table(at(5, 27), "x", eq, slopeeq, range(2, 1.5, 1.1, 1.01, 1.001), type(1))
```
