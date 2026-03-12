---
title: asa
sidebar_label: asa
---

# asa

Constructs a triangle from two angles and the included side between them (Angle-Side-Angle), automatically computing the third angle and remaining sides.

**Utility:** Create triangle from two angles and the included side between them

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container created with g2d() |
| `angleA` | `number (degrees)` | Yes | Angle at vertex A in degrees |
| `c` | `number` | Yes | Length of side from A to B (the included side) |
| `angleB` | `number (degrees)` | Yes | Angle at vertex B in degrees (angleA + angleB must be &lt; 180) |
| `basePoint` | `point \| point(G, x, y)` | No | Position for vertex A (defaults to origin) |
| `angle` | `number` | No | Rotation angle in degrees for the entire triangle |

## Variants

### Basic ASA triangle

```js
asa(G, angleA, sideC, angleB)
```

Triangle at origin with two angles and included side

### Positioned triangle

```js
asa(G, 45, 5, 60, point(G, 0, 0))
```

Triangle positioned at specific point

### Equilateral via angles

```js
asa(G, 60, 5, 60)
```

Equilateral triangle (all angles 60 degrees)

### Isosceles via angles

```js
asa(G, 70, 4, 70)
```

Isosceles triangle with equal base angles

## Examples

### ASA triangle for sine rule demonstration

```js
triangle_1 = asa(graph_1, 45, 5, 60, point(graph_1, 0, 0))
```

### Extract angle at vertex A

```js
angle_A = angle(graph_1, item(triangle_1, type(angle), 1), 0.8)
```

### Extract angle at vertex B

```js
angle_B = angle(graph_1, item(triangle_1, type(angle), 2), 0.8)
```

### Extract the included side

```js
line_c = line(graph_1, item(triangle_1, type(edge), 1), type(segment), c(blue))
```

### Equilateral triangle construction

```js
triangle_eq = asa(graph_1, 60, 4, 60, point(graph_1, 2, 2))
```
