---
title: reflect
sidebar_label: reflect
---

# reflect

Creates a mirror image of a geometric shape across a line axis. The reflected shape preserves all distances and angles (isometric transformation).

**Utility:** Reflect a shape across a line creating a mirror image

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | The 2D graph container |
| `line` | `line` | Yes | Line to reflect across (the mirror axis) |
| `shape` | `point \| line \| circle \| polygon` | Yes | Shape to reflect |

## Variants

### Reflect a point

```js
reflect(G, axis, P)
```

Mirror image of point P across line axis

### Reflect a line

```js
reflect(G, axis, L)
```

Mirror image of line L across line axis

### Reflect a circle

```js
reflect(G, axis, C)
```

Mirror image of circle C across line axis

### Reflect a polygon

```js
reflect(G, axis, T)
```

Mirror image of polygon T across line axis

## Examples

### Set up graph for reflection

```js
graph_1 = g2d(at(10, 10), 20, 20)
```

### Create a vertical axis of reflection

```js
axis = vline(graph_1, 0)
```

### Create a point to reflect

```js
P = point(graph_1, 3, 2)
```

### Reflect point across axis

```js
P_reflected = reflect(graph_1, axis, P)
```

### Create a triangle and reflect it

```js
T = sas(graph_1, 3, 60, 4, point(graph_1, 1, 1))
```

### Reflect triangle across axis for symmetry

```js
T_reflected = reflect(graph_1, axis, T)
```

### Reflect a circle across a diagonal line

```js
diag = line(graph_1, point(graph_1, -5, -5), point(graph_1, 5, 5))
```

### Create and reflect a circle

```js
C = circle(graph_1, point(graph_1, 3, 0), radius(2))
```

### Mirror the circle across the diagonal

```js
C_reflected = reflect(graph_1, diag, C)
```
