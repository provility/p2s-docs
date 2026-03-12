---
title: overbrace
sidebar_label: overbrace
---

# overbrace

Draw a curly brace above a selected sub-expression to annotate grouped terms, indicate operation scope, or add explanatory notes. Supports adjustable vertical spacing, stroke color, and width.

**Utility:** Draw a curly brace above a text selection for annotation

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `target` | `TextItem variable` | Yes | A TextItem variable from select() to place the overbrace above |
| `buffer` | `number` | No | Vertical distance above the text item in pixels (default: 5) |
| `color` | `c(colorName)` | No | Stroke color for the brace - e.g., c(blue), c(red) |
| `strokeWidth` | `s(number)` | No | Stroke width for the brace - e.g., s(3) |

## Variants

### Basic overbrace

```js
overbrace(T)
```

Draw default overbrace above text item T

### With buffer

```js
overbrace(T, 10)
```

Overbrace with custom vertical spacing

### Colored overbrace

```js
overbrace(T, c(blue))
```

Blue overbrace above text item

### Buffer with styling

```js
overbrace(T, 10, c(red), s(3))
```

Custom buffer with red color and thick stroke

### Marker syntax

```js
marker(at(target, type(top)), type(overbrace))
```

Unified marker syntax for overbrace

## Examples

### Overbrace grouped terms in a sum

```js
W = write(at(5, 3), "a + b + c + d", type(write))
sel = select(W, "a + b", 1)
overbrace_1 = overbrace(sel)
```

### Overbrace with custom spacing and blue color

```js
sel = select(write_1, "x^2 + 2x", 1)
overbrace_2 = overbrace(sel, 10, c(blue))
```

### Overbrace with red styling and thick stroke

```js
sel = select(write_1, "sin(theta)", 1)
overbrace_3 = overbrace(sel, c(red), s(3))
```

### Annotate discriminant from above

```js
Q = write(at(6, 4), "x = (-b +- sqrt(b^2 - 4ac)) / (2a)", type(write))
D = select(Q, "b^2 - 4ac", 1)
overbrace_4 = overbrace(D, 8, c(green))
```
