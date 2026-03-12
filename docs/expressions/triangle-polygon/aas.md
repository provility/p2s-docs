---
title: aas
sidebar_label: aas
---

# aas

Constructs a triangle from two angles and a non-included side (Angle-Angle-Side), automatically computing the third angle and remaining sides via the law of sines.

**Utility:** Create triangle from two angles and a non-included side opposite to first angle

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container created with g2d() |
| `angleA` | `number (degrees)` | Yes | Angle at vertex A in degrees |
| `angleB` | `number (degrees)` | Yes | Angle at vertex B in degrees (angleA + angleB must be &lt; 180) |
| `a` | `number` | Yes | Length of side opposite to angle A (from B to C) |
| `basePoint` | `point \| point(G, x, y)` | No | Position for vertex A (defaults to origin) |
| `angle` | `number` | No | Rotation angle in degrees for the entire triangle |

## Variants

### Basic AAS triangle

```js
aas(G, angleA, angleB, sideA)
```

Triangle at origin with two angles and opposite side

### Positioned triangle

```js
aas(G, 30, 60, 5, point(G, 0, 0))
```

Triangle positioned at specific point

### 30-60-90 triangle

```js
aas(G, 30, 60, 5)
```

Special right triangle with known angles

## Examples

### AAS triangle with two given angles and opposite side

```js
triangle_1 = aas(graph_1, 30, 60, 5, point(graph_1, 0, 0))
```

### Extract all three angles for comparison

```js
angle_A = angle(graph_1, item(triangle_1, type(angle), 1), 0.8)
```

### Label the given angle A

```js
label_A = label(graph_1, at(angle_A), "30", buff(-0.5, 0.5))
```

### Extract and measure the given side a

```js
line_a = line(graph_1, item(triangle_1, type(edge), 2), type(segment), c(blue))
```

### Special 30-60-90 triangle

```js
triangle_special = aas(graph_1, 30, 60, 4, point(graph_1, 3, 3))
```
