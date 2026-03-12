---
title: at
sidebar_label: at
---

# at

Set the absolute position of a container on the canvas using logical row and column coordinates.

**Utility:** Position containers at absolute logical row/col coordinates on the canvas

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `row` | `number` | Yes | Vertical position in logical units (0 = top, increases downward) |
| `col` | `number` | Yes | Horizontal position in logical units (0 = left, increases rightward) |

## Variants

### Position a graph

```js
g2d(at(row, col), width, height)
```

Place a 2D graph at row, col

### Position a 3D scene

```js
g3d(at(row, col), width, height)
```

Place a 3D scene at row, col

### Position math text

```js
write(at(row, col), "expression", type(write))
```

Place written math at row, col

### Position a table

```js
table(at(row, col), "x", equation, range(...))
```

Place a table at row, col

### Position an input

```js
input(at(row, col), value(...), "label")
```

Place an input dropdown at row, col

### Side-by-side layout

```js
G1 = g2d(at(2, 2), 14, 14)
G2 = g2d(at(2, 18), 14, 14)
```

Two graphs side by side using different col values

### Stacked layout

```js
G1 = g2d(at(2, 2), 14, 14)
G2 = g2d(at(18, 2), 14, 14)
```

Two graphs stacked using different row values

## Examples

### Graph positioned at top-left area

```js
G = g2d(at(2, 3), 30, 30)
```

### Graph with axes positioned with offset

```js
graph_1 = g2d(at(5, 26), 13.3, 20.6, range(-1, 5, 1), range(-1, 5, 1), grid(noaxes))
```

### Write math text at specific position

```js
write_1 = write(at(3.1, 2.2), "int sqrt(a^2-x^2) dx", type(write))
```

### Table positioned beside a graph

```js
t = table(at(1, 7), "x", eq, slopeeq, range(2, 1.5, 1.1, 1.01, 1.001), c(blue))
```

### Grid of 6 graphs (2 rows x 3 cols)

```js
G1 = g2d(at(2, 2), 14, 14)
G2 = g2d(at(2, 18), 14, 14)
G3 = g2d(at(2, 34), 14, 14)
G4 = g2d(at(18, 2), 14, 14)
G5 = g2d(at(18, 18), 14, 14)
G6 = g2d(at(18, 34), 14, 14)
```

### 3D scene at origin

```js
S = g3d(at(0, 0), 30, 30, type(3))
```

### Write text below a graph

```js
G = g2d(at(2, 3), 14, 14)
write_1 = write(at(18, 3), "f(x) = x^2", type(write))
```

### Input dropdown above a graph

```js
eq1 = input(at(0, 2), value("a*x^2 + b*x + c", "a*sin(b*x)"), "f(x)")
G1 = g2d(at(2, 2), 14, 14)
```
