---
title: tangentplane
sidebar_label: tangentplane
---

# tangentplane

Computes and displays the tangent plane to a 3D surface at a given point using partial derivatives for linear approximation.

**Utility:** Display the tangent plane to a 3D surface at a given point

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g3d reference` | Yes | The 3D graph container |
| `surface` | `plot3d reference \| string` | Yes | The surface to compute tangent plane for - either a plot3d variable or a quoted equation string |
| `x` | `number \| point3d` | Yes | x-coordinate of tangent point, or a point3d reference |
| `y` | `number` | No | y-coordinate of tangent point (not needed if using point3d) |
| `size` | `number` | No | Visual size of the tangent plane (default 4) |

## Variants

### Tangent plane on plot3d reference with x, y

```js
tangentplane(G, surface, x, y)
```

Tangent plane at coordinates (x, y) on a plot3d surface

### Tangent plane on plot3d reference with size

```js
tangentplane(G, surface, x, y, size)
```

Tangent plane with custom visual size

### Tangent plane at point3d

```js
tangentplane(G, surface, pt)
```

Tangent plane at a point3d location (uses x, y from point)

### Tangent plane at point3d with size

```js
tangentplane(G, surface, pt, size)
```

Tangent plane at point3d with custom visual size

### Tangent plane from string equation

```js
tangentplane(G, "x^2 + y^2", x, y)
```

Tangent plane using inline string equation instead of plot3d reference

## Examples

### Tangent plane on paraboloid with animated point

```js
G = g3d(at(0, 0), 30, 30)
S = plot3d(G, "x^2 + y^2", range(-3, 3), range(-3, 3))
tx = 1
ty = 1
pt = point3d(G, tx, ty, tx*tx + ty*ty)
T = tangentplane(G, S, pt)
change(tx, 1, -2)
```

### Tangent plane using function definition and coordinates

```js
G = g3d(at(0, 0), 30, 30)
f = def(x, y, "x^2 + y^2")
P = plot3d(G, f, range(-3, 3), range(-3, 3))
x0 = 1
y0 = 1
T = tangentplane(G, P, x0, y0)
change(x0, 1, -2)
```
