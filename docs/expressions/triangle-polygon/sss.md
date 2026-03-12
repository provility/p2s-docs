---
title: sss
sidebar_label: sss
---

# sss

Construct a triangle from three side lengths (Side-Side-Side), or a right triangle from two leg lengths. Automatically computes vertex positions and angles.

**Utility:** Create right triangle from two leg lengths with automatic hypotenuse

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container created with g2d() |
| `a` | `number` | Yes | Length of first leg (extends along x-axis from right angle vertex) |
| `b` | `number` | Yes | Length of second leg (extends perpendicular to first leg) |
| `basePoint` | `point \| point(G, x, y)` | Yes | Position for vertex A (right angle vertex) |
| `angle` | `number` | No | Rotation angle in degrees (rotates entire triangle around basePoint) |

## Variants

### Basic right triangle

```js
sss(G, a, b, point(G, x, y))
```

Right triangle with legs a and b at specified position

### 3-4-5 triangle

```js
sss(G, 3, 4, P)
```

Classic Pythagorean triple triangle at point P

### Rotated triangle

```js
sss(G, a, b, P, 45)
```

Triangle rotated 45 degrees around basePoint

### From line lengths

```js
sss(G, distance(L1), distance(L2), O)
```

Triangle with legs equal to existing line lengths

### Hidden stroke

```js
sss(G, 3, 4, P, so(0))
```

Create triangle structure without visible outline (for extraction)

## Examples

### Pythagorean theorem demonstration with 3-4-5 triangle

```js
triangle_1 = sss(graph_1, 3, 4, point(graph_1, 0, 0))
```

### Extract and label the right angle

```js
angle_A = angle(graph_1, item(triangle_1, type(angle), 1), 0.8)
```

### Extract edge as line for measurement

```js
line_a = line(graph_1, item(triangle_1, type(edge), 1), type(segment), c(blue))
```

### Isosceles right triangle rotated 45 degrees

```js
triangle_2 = sss(graph_1, 5, 5, point(graph_1, 2, 2), 45)
```

### Hidden triangle for extracting components only

```js
triangle_3 = sss(graph_1, 3, 4, point(graph_1, 0, 0), so(0))
```
