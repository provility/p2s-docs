---
title: tangent
sidebar_label: tangent
---

# tangent

Draws a tangent line to a curve or circle at a specified point, centered at the point of tangency. Used for visualizing instantaneous slope, derivatives, and linear approximation.

**Utility:** Draw a tangent line to a curve at a specific x-value

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d reference` | Yes | The 2D graph container |
| `plotVariable` | `plot reference` | Yes | A previously assigned plot variable |
| `x` | `number` | Yes | The x-coordinate where the tangent touches the curve |
| `buff` | `buff(value)` | No | Visual extent adjustment - e.g., buff(0.3) |
| `color` | `c(colorName)` | No | Line color - e.g., c(blue) |

## Variants

### Tangent to a plot at x

```js
f = plot(G, "f(x)")
tangent(G, f, x)
```

Tangent line to f at the given x-value

### Tangent with visual extent

```js
f = plot(G, "f(x)")
tangent(G, f, x, buff(0.3))
```

Tangent line with adjusted display length

### Tangent with color

```js
f = plot(G, "f(x)")
tangent(G, f, x, c(blue))
```

Colored tangent line

### Tangent to a circle at angle

```js
C = circle(G, 3, pt)
tangent(G, C, 45)
```

Tangent line to circle at 45 degrees

## Examples

### Tangent to x^2 at x = 1

```js
G = g2d(at(2, 2), 30, 30)
f = plot(G, "x^2")
t = tangent(G, f, 1, buff(0.3))
```

### Tangent with secant approaching (limit definition of derivative)

```js
eq = def(x, "x^2")
G = g2d(at(2, 3), 30, 30, range(-2, 3), range(-1, 5))
pl1 = plot(G, eq)
tangent(G, pl1, 0.8, c(blue))
p = point(G, 0.8, fun(eq, 0.8))
label(G, p, "P", buff(-1, 1))
q_1 = 2
q = point(G, q_1, fun(eq, q_1))
label(G, q, "Q", buff(-1, -1))
line(G, p, q, c(red))
change(q_1, 0.8, t(5))
```

### Tangent to a plot with color styling

```js
G = g2d(at(2, 2), 30, 30)
f = plot(G, "sin(x)")
tangent(G, f, 1.57, c(red))
```
