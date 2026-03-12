---
title: ellipse
sidebar_label: ellipse
---

# ellipse

Draws an ellipse on a 2D graph from center coordinates and semi-axes, or from a standard-form equation string. Supports optional rotation in radians.

**Utility:** Draw an ellipse on a 2D graph by center+axes or equation

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | The 2D graph container to draw on |
| `center` | `point \| two numbers (cx, cy)` | Yes | Center of the ellipse - either a point expression or two coordinate values |
| `a` | `number` | Yes | Semi-major axis length (along the rotation direction). Must be positive |
| `b` | `number` | Yes | Semi-minor axis length (perpendicular to rotation). Must be positive |
| `rotation` | `number (radians)` | No | Rotation angle in radians. Defaults to 0 (horizontal) |
| `equation` | `string` | No | Alternative to parametric args - standard form equation string e.g. "x^2/25 + y^2/9 = 1" |

## Variants

### Center point + semi-axes

```js
ellipse(G, center_point, a, b)
```

Ellipse at a point with semi-axes a and b

### Center coordinates + semi-axes

```js
ellipse(G, cx, cy, a, b)
```

Ellipse at coordinates (cx, cy) with semi-axes a and b

### With rotation

```js
ellipse(G, center_point, a, b, rotation)
```

Rotated ellipse, angle in radians

### From equation string

```js
ellipse(G, "x^2/25 + y^2/9 = 1")
```

Ellipse defined by standard-form equation

### Shifted equation

```js
ellipse(G, "(x-2)^2/9 + (y+1)^2/4 = 1")
```

Ellipse centered at (2, -1) from equation

## Examples

### Ellipse at origin with semi-axes 4 and 2

```js
E = ellipse(G, 4, 2, point(G, 0, 0))
```

### Ellipse from equation

```js
E = ellipse(G, "x^2/25 + y^2/9 = 1")
```

### Shifted ellipse from equation

```js
E = ellipse(G, "(x-2)^2/9 + (y+1)^2/4 = 1")
```

### Extract and draw foci of an ellipse

```js
F1 = point(G, property(E, type(foci, 1)), c(red))
```

### Extract and draw second focus

```js
F2 = point(G, property(E, type(foci, 2)), c(red))
```

### Draw a vertex of the ellipse

```js
V1 = point(G, property(E, type(vertex, 1)), c(green))
```

### Sample a point on the ellipse at ratio t

```js
P = point(G, E, 0.5, type(ratio))
```

### Animate focal distance trace

```js
trace_1 = trace(G, E, type(focal), 0, 360, buff(-1, -1))
```
