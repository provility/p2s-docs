---
title: angle
sidebar_label: angle
---

# angle

Draws an angle arc at a vertex between two rays, supporting interior, exterior, reflex, and right angle types with automatic 90-degree square marker detection.

**Utility:** Create angle arc visualization at vertex between two rays

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container created with g2d() |
| `vertex` | `point \| item() result` | Yes | Vertex point where angle is measured (or item() extraction) |
| `point1` | `point` | Yes | First ray endpoint (if not using item()) |
| `point2` | `point` | Yes | Second ray endpoint (if not using item()) |
| `radius` | `number` | No | Radius of angle arc (default 0.8, smaller for right angles) |
| `type` | `type(interior\|ext1\|ext2\|reflex\|opposite\|right)` | No | Angle type: interior (default), ext1/ext2 (exterior), reflex (&gt;180), right (force square marker) |

## Variants

### From three points

```js
angle(G, vertex, point1, point2)
```

Angle arc at vertex between two points

### From item() extraction

```js
angle(G, item(triangle, type(angle), 1), 0.8)
```

Angle at first vertex of triangle

### With custom radius

```js
angle(G, V, P1, P2, 0.5)
```

Smaller angle arc

### Interior angle

```js
angle(G, V, P1, P2, type(interior))
```

Explicit interior angle (default)

### Exterior angle

```js
angle(G, V, P1, P2, type(ext1))
```

First exterior angle

### Right angle marker

```js
angle(G, V, P1, P2, type(right))
```

Force right angle square marker

## Examples

### Create triangle and mark all angles

```js
triangle_1 = sas(graph_1, 5, 40, 6, point(graph_1, 0, 0))
```

### Extract and draw angle at vertex 1

```js
angle_A = angle(graph_1, item(triangle_1, type(angle), 1), 0.8)
```

### Extract and draw angle at vertex 2

```js
angle_B = angle(graph_1, item(triangle_1, type(angle), 2), 0.8)
```

### Extract and draw angle at vertex 3

```js
angle_C = angle(graph_1, item(triangle_1, type(angle), 3), 0.8)
```

### Angle from three explicit points

```js
angle_1 = angle(graph_1, point_B, point_A, point_C, 0.8, type(interior))
```

### Right angle marker (auto-detected for 90 degrees)

```js
angle_right = angle(graph_1, item(sss_triangle, type(angle), 1), 0.35)
```

### Exterior angle

```js
angle_ext = angle(graph_1, P1, P2, P3, 0.8, type(ext1))
```

### Colored angle arc

```js
angle_A = angle(graph_1, item(triangle_1, type(angle), 1), 0.8, c(blue))
```
