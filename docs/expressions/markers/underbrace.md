---
title: underbrace
sidebar_label: underbrace
---

# underbrace

Draw a curly brace below a selected sub-expression to annotate grouped terms, show substitutions, or add notes beneath. Supports adjustable vertical spacing, stroke color, and width.

**Utility:** Draw a curly brace below a text selection for annotation

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `target` | `TextItem variable` | Yes | A TextItem variable from select() to place the underbrace below |
| `buffer` | `number` | No | Vertical distance below the text item in pixels (default: 5) |
| `color` | `c(colorName)` | No | Stroke color for the brace - e.g., c(blue), c(red) |
| `strokeWidth` | `s(number)` | No | Stroke width for the brace - e.g., s(3) |

## Variants

### Basic underbrace

```
underbrace(T)
```

Draw default underbrace below text item T

### With buffer

```
underbrace(T, -10)
```

Underbrace with custom vertical spacing

### Colored underbrace

```
underbrace(T, c(blue))
```

Blue underbrace below text item

### Buffer with styling

```
underbrace(T, 10, c(red), s(3))
```

Custom buffer with red color and thick stroke

### Marker syntax

```
marker(at(target, type(bottom)), type(underbrace))
```

Unified marker syntax for underbrace

## Examples

### Underbrace terms in a polynomial

```
W = write(at(5, 3), "x^2 + 2x + 1", type(write))
sel = select(W, "2x + 1", 1)
underbrace_1 = underbrace(sel)
```

### Underbrace with blue color for substitution label

```
sel = select(write_1, "a cos(theta)", 1)
underbrace_2 = underbrace(sel, c(blue))
```

### Underbrace with buffer and red thick stroke

```
sel = select(write_1, "sqrt(a^2-x^2)", 1)
underbrace_3 = underbrace(sel, -10, c(red), s(3))
```

### Annotate denominator from below

```
Q = write(at(6, 4), "x = (-b +- sqrt(b^2 - 4ac)) / (2a)", type(write))
D = select(Q, "2a", 1)
underbrace_4 = underbrace(D, 8, c(green))
```
