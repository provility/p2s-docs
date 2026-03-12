---
title: measure
sidebar_label: measure
---

# measure

Display a distance measurement annotation between two points or along a line segment, with end markers and an auto-centered text label. Supports perpendicular offset for clean placement and custom or computed distance labels.

**Utility:** Create measurement annotation between two points with distance label

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container created with g2d() |
| `target` | `line \| point1, point2` | Yes | A line variable, or two point variables to measure between |
| `text` | `string` | No | Label text for measurement (optional, shows computed distance if omitted) |
| `buff` | `buff(x, y)` | No | Perpendicular offset for entire marker in model units |
| `color` | `c(colorName)` | No | Color for measurement line and markers - e.g., c(black), c(red) |

## Variants

### Measure a line

```js
measure(G, line_var)
```

Measurement indicator on existing line variable

### Measure between points

```js
measure(G, P1, P2)
```

Measurement between two point variables

### Measure with offset

```js
measure(G, line_var, buff(0, -1))
```

Measurement offset perpendicular to line

### Measure with label

```js
measure(G, line_var, "5 cm", buff(0, -0.5))
```

Measurement with custom text label and offset

### Colored measurement

```js
measure(G, line_var, buff(0, -1), c(black))
```

Measurement with specific color

### Measure between points with label and offset

```js
measure(G, P1, P2, "", buff(1.7, 1))
```

Two-point measurement with empty label and offset

## Examples

### Measure between two points with offset (from label-markers lesson)

```js
point_3 = point(graph_1, 2.0, -1.7)
point_4 = point(graph_1, -3.3, -2.1)
measure_1 = measure(graph_1, point_3, point_4, "", buff(1.7, 1))
```

### Measure a triangle side with offset and color

```js
measure_a = measure(graph_1, line_a, buff(0, -1), c(black))
```

### Measure with custom label text

```js
measure_b = measure(graph_1, line_b, "5 units", buff(0, -0.5))
```

### Measure extracted edge from polygon

```js
edge_line = line(graph_1, item(triangle_1, type(edge), 1), type(segment))
edge_measure = measure(graph_1, edge_line, buff(0, -0.5))
```

### Hide measurements initially for reveal animation

```js
measure_a = measure(graph_1, line_a, buff(0, -1))
measure_b = measure(graph_1, line_b, buff(0, -0.5))
hide(measure_a, measure_b)
```
