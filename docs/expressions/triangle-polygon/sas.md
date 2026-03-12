---
title: sas
sidebar_label: sas
---

# sas

Construct a triangle from two sides and the included angle between them (Side-Angle-Side). Automatically computes the third side and remaining angles.

**Utility:** Create triangle from two sides and the included angle between them

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container created with g2d() |
| `b` | `number` | Yes | Length of side from A to C (opposite vertex B) |
| `angleA` | `number (degrees)` | Yes | Angle at vertex A in degrees (between 0 and 180) |
| `c` | `number` | Yes | Length of side from A to B (opposite vertex C) |
| `basePoint` | `point \| point(G, x, y)` | No | Position for vertex A (defaults to origin) |
| `angle` | `number` | No | Rotation angle in degrees for the entire triangle |

## Variants

### Basic SAS triangle

```js
sas(G, b, angleA, c)
```

Triangle at origin with two sides and included angle

### Positioned triangle

```js
sas(G, 5, 40, 6, point(G, 0, 0))
```

Triangle positioned at specific point

### Right triangle

```js
sas(G, 4, 90, 3)
```

Right triangle using 90-degree angle

### Isosceles with angle

```js
sas(G, 5, 60, 5)
```

Isosceles triangle with equal sides and 60-degree angle

### Rotated triangle

```js
sas(G, 5, 40, 6, P, 30)
```

Triangle rotated 30 degrees from horizontal

## Examples

### Sine law demonstration triangle

```js
triangle_1 = sas(graph_1, 5, 40, 6, point(graph_1, 0, 0))
```

### Extract all three edges for labeling

```js
line_c = line(graph_1, item(triangle_1, type(edge), 1), type(segment), c(blue))
```

### Extract angle at vertex A for measurement

```js
angle_A = angle(graph_1, item(triangle_1, type(angle), 1), 0.8)
```

### Label the angle A

```js
label_A = label(graph_1, at(angle_A), "A", buff(-1.0, 1.0))
```

### Measure side length with offset

```js
measure_a = measure(graph_1, line_a, buff(0, -1), c(black))
```
