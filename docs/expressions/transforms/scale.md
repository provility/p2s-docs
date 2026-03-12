---
title: scale
sidebar_label: scale
---

# scale

Scales a geometric shape uniformly by a given factor around a center point, where factors greater than 1 enlarge and between 0 and 1 shrink.

**Utility:** Scale a shape by a factor around a center point

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | The graph container |
| `shape` | `point \| line \| circle \| polygon \| image` | Yes | The shape to scale |
| `factor` | `number` | Yes | Scale factor (&gt;1 enlarges, 0-1 shrinks, negative reflects) |
| `cx, cy` | `number, number` | No | Center of scaling as x, y coordinates (default: origin) |
| `centerPoint` | `point` | No | Center of scaling as a point expression (alternative to cx, cy) |

## Variants

### Scale around origin

```js
scale(G, shape, factor)
```

Scale shape around origin (0,0) by the given factor

### Scale around coordinates

```js
scale(G, shape, factor, cx, cy)
```

Scale shape around explicit center (cx, cy)

### Scale around point expression

```js
scale(G, shape, factor, centerPoint)
```

Scale shape around a point expression

## Examples

### Scale a triangle by factor 2 from the origin

```js
T = sas(G, 3, 60, 3, point(G, 1, 1))
T2 = scale(G, T, 2)
```

### Shrink a circle by half around its center

```js
center = point(G, 3, 3)
C = circle(G, 4, center)
C2 = scale(G, C, 0.5, center)
```

### Scale a polygon around a specific point

```js
P = polygon(G, point(G, 0, 0), point(G, 4, 0), point(G, 4, 3), point(G, 0, 3))
P2 = scale(G, P, 1.5, 2, 1.5)
```

### Scale a line segment by factor 3 from origin

```js
L = line(G, 1, 0, 2, 0)
L2 = scale(G, L, 3)
```

### Negative scale to reflect and enlarge

```js
P = point(G, 2, 3)
P2 = scale(G, P, -1)
```
