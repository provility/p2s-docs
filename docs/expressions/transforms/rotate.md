---
title: rotate
sidebar_label: rotate
---

# rotate

Rotates a geometric shape around a center point by a specified angle in degrees, with positive angles rotating counter-clockwise.

**Utility:** Rotate a shape around a center point by a specified angle in degrees

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | The graph container |
| `shape` | `point \| line \| circle \| polygon \| image` | Yes | The shape to rotate |
| `angle` | `number` | Yes | Rotation angle in degrees (positive = counter-clockwise) |
| `cx, cy` | `number, number` | No | Center of rotation as x, y coordinates (default: origin) |
| `centerPoint` | `point` | No | Center of rotation as a point expression (alternative to cx, cy) |

## Variants

### Rotate around origin

```js
rotate(G, shape, angle)
```

Rotate shape around origin (0,0) by angle degrees

### Rotate around coordinates

```js
rotate(G, shape, angle, cx, cy)
```

Rotate shape around explicit center point (cx, cy)

### Rotate around point expression

```js
rotate(G, shape, angle, centerPoint)
```

Rotate shape around a point expression

## Examples

### Rotate a point 45 degrees around the origin

```js
P = point(G, 3, 0)
R = rotate(G, P, 45)
```

### Rotate a line 90 degrees around a specific center

```js
L = line(G, 0, 0, 3, 0)
R = rotate(G, L, 90, 1.5, 0)
```

### Rotate a polygon around one of its vertices

```js
P1 = point(G, 0, 0)
T = sas(G, 5, 40, 6, P1)
R = rotate(G, T, 60, P1)
```

### Animate an image translation (from image-rotation lesson)

```js
G = g2d(at(2, 20), 20, 20)
I = image(G, "balloon", point(G, -5, 0), 0.1)
R = translate(G, I, 4, a)
animator(at(10,10), a, 2)
```

### Rotate a circle around a custom center point

```js
C = circle(G, 2, point(G, 3, 0))
center = point(G, 0, 0)
R = rotate(G, C, 120, center)
```
