---
title: hyperbola
sidebar_label: hyperbola
---

# hyperbola

Draws a two-branch hyperbola on a 2D graph from center coordinates and transverse/conjugate semi-axes, or from a standard-form equation string. Supports optional rotation in radians.

**Utility:** Draw a hyperbola on a 2D graph by center+axes or equation

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | The 2D graph container to draw on |
| `center` | `point \| two numbers (h, k)` | Yes | Center of the hyperbola - either a point expression or two coordinate values |
| `a` | `number` | Yes | Semi-transverse axis length (along rotation direction, where vertices are). Must be positive |
| `b` | `number` | Yes | Semi-conjugate axis length (perpendicular). Must be positive |
| `rotation` | `number (radians)` | No | Rotation angle in radians. Defaults to 0 (horizontal transverse axis) |
| `equation` | `string` | No | Alternative to parametric args - standard form equation string e.g. "x^2/16 - y^2/9 = 1" |

## Variants

### Center point + semi-axes

```
hyperbola(G, center_point, a, b)
```

Hyperbola at a point with transverse axis a and conjugate axis b

### Center coordinates + semi-axes

```
hyperbola(G, h, k, a, b)
```

Hyperbola at (h, k) with semi-axes a and b

### With rotation

```
hyperbola(G, center_point, a, b, rotation)
```

Rotated hyperbola, angle in radians

### From equation string

```
hyperbola(G, "x^2/16 - y^2/9 = 1")
```

Hyperbola defined by standard-form equation

### Shifted equation

```
hyperbola(G, "(x-1)^2/4 - (y+2)^2/9 = 1")
```

Hyperbola centered at (1, -2) from equation

## Examples

### Hyperbola at origin with semi-axes 3 and 2

```
H = hyperbola(G, point(G, 0, 0), 3, 2)
```

### Hyperbola from equation

```
H = hyperbola(G, "x^2/16 - y^2/9 = 1")
```

### Extract and draw first focus

```
F1 = point(G, property(H, type(foci, 1)), c(red))
```

### Extract and draw second focus

```
F2 = point(G, property(H, type(foci, 2)), c(red))
```

### Draw first vertex

```
V1 = point(G, property(H, type(vertex, 1)), c(green))
```

### Draw first directrix line

```
D1 = line(G, property(H, type(directrix, 1)))
```

### Animate focal difference trace

```
trace_1 = trace(G, H, type(1), buff(-1, -1))
```

### Sample point on hyperbola at ratio

```
P = point(G, H, 0.25, type(ratio))
```
