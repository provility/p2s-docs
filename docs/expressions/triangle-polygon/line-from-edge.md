---
title: line (from edge)
sidebar_label: line (from edge)
---

# line (from edge)

Creates a visible line from edge data extracted from a polygon or triangle. Supports segment (finite), line (infinite), and ray (half-infinite) rendering modes, with optional color and dash styling.

**Utility:** Draw visible line from polygon edge extraction

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container created with g2d() |
| `edge_data` | `item(polygon, type(edge), index)` | Yes | Edge data extracted from polygon using item() |
| `lineType` | `type(segment) \| type(line) \| type(ray)` | No | Type of line: segment (default), line (infinite), ray |

## Variants

### Line segment from edge

```js
line(G, item(triangle, type(edge), 1), type(segment))
```

Finite line segment matching edge

### Infinite line through edge

```js
line(G, item(triangle, type(edge), 1), type(line))
```

Line extending infinitely through edge

### Colored edge

```js
line(G, item(triangle, type(edge), 1), type(segment), c(blue))
```

Blue line segment from edge

### Dashed edge

```js
line(G, item(triangle, type(edge), 1), type(segment), dash())
```

Dashed line segment from edge

## Examples

### Create triangle and extract all edges

```js
triangle_1 = sas(graph_1, 5, 40, 6, point(graph_1, 0, 0))
```

### Draw edge c (first edge) in blue

```js
line_c = line(graph_1, item(triangle_1, type(edge), 1), type(segment), c(blue))
```

### Draw edge a (second edge) in blue

```js
line_a = line(graph_1, item(triangle_1, type(edge), 2), type(segment), c(blue))
```

### Draw edge b (third edge) in blue

```js
line_b = line(graph_1, item(triangle_1, type(edge), 3), type(segment), c(blue))
```

### Highlight base edge with thick stroke

```js
stroke_line_c = stroke(line_c, type(width), 8)
```

### Draw height as dashed red line

```js
line_height = line(graph_1, point_c, point_projected_d, type(segment), dash(), c(red))
```
