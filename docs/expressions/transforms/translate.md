---
title: translate
sidebar_label: translate
---

# translate

Translates a geometric shape by a displacement vector (dx, dy), moving every point the same distance in the same direction.

**Utility:** Shift a shape by a displacement vector (dx, dy)

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | The graph container |
| `shape` | `point \| line \| circle \| polygon \| plot \| image` | Yes | The shape to translate |
| `dx` | `number` | Yes | Horizontal displacement (positive = right) |
| `dy` | `number` | Yes | Vertical displacement (positive = up) |

## Variants

### Translate with numeric values

```
translate(G, shape, dx, dy)
```

Shift shape by (dx, dy)

## Examples

### Translate a point 3 units right and 2 units up

```
P = point(G, 1, 1)
T = translate(G, P, 3, 2)
```

### Translate an image with animation (from image-rotation lesson)

```
G = g2d(at(2, 20), 20, 20)
I = image(G, "balloon", point(G, -5, 0), 0.1)
R = translate(G, I, 4, a)
animator(at(10,10), a, 2)
```

### Translate a polygon to create a copy

```
T = sas(G, 5, 60, 5, point(G, 0, 0))
T2 = translate(G, T, 6, 0)
```

### Translate a circle diagonally

```
C = circle(G, 3, point(G, 0, 0))
C2 = translate(G, C, 4, 4)
```

### Translate a line segment vertically

```
L = line(G, 0, 0, 3, 2)
L2 = translate(G, L, 0, 4)
```
