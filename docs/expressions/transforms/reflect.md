---
title: reflect
sidebar_label: reflect
---

# reflect

Reflects a geometric shape across a line of symmetry to create its mirror image.

**Utility:** Create a mirror image of a shape reflected across a line

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | The graph container |
| `line` | `line` | Yes | The line to reflect across (axis of symmetry) |
| `shape` | `point \| line \| circle \| polygon` | Yes | The shape to reflect |

## Variants

### Reflect point across line

```js
reflect(G, mirrorLine, point)
```

Reflect a point across a line of symmetry

### Reflect polygon across line

```js
reflect(G, mirrorLine, polygon)
```

Reflect an entire polygon across a line

## Examples

### Reflect a point across the x-axis

```js
xAxis = line(G, -5, 0, 5, 0)
P = point(G, 2, 3)
R = reflect(G, xAxis, P)
```

### Reflect a triangle across a vertical line

```js
mirror = line(G, 0, -5, 0, 5)
T = sas(G, 4, 60, 4, point(G, 1, 1))
R = reflect(G, mirror, T)
```

### Reflect a circle across a diagonal line

```js
L = line(G, 0, 0, 5, 5)
C = circle(G, 2, point(G, 3, 0))
R = reflect(G, L, C)
```

### Create a symmetric design by reflecting a polygon

```js
axis = line(G, 0, -5, 0, 5)
P = polygon(G, point(G, 1, 0), point(G, 3, 2), point(G, 2, 4))
R = reflect(G, axis, P, c(blue))
```

### Reflect a line segment across another line

```js
mirror = line(G, -3, -3, 3, 3)
L = line(G, 1, 0, 4, 0)
R = reflect(G, mirror, L)
```
