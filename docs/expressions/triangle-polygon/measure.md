---
title: measure
sidebar_label: measure
---

# measure

Displays a dimensioned measurement indicator showing the distance between two points or along a line, with end markers and an optional centered text label. Supports perpendicular offset positioning for clean diagram layout.

**Utility:** Create measurement indicator between two points or along a line

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container created with g2d() |
| `line or points` | `line \| point1, point2` | Yes | Line variable or two points to measure between |
| `text` | `string` | No | Label text for measurement (optional, displays length if omitted) |
| `buff` | `buff(x, y)` | No | Perpendicular offset for entire marker in model units |

## Variants

### Measure a line

```js
measure(G, line_a)
```

Measurement indicator on existing line

### Measure with offset

```js
measure(G, line_a, buff(0, -1))
```

Measurement indicator offset from line

### Measure with label

```js
measure(G, line_a, "5 cm", buff(0, -0.5))
```

Measurement with custom text label

### Measure between points

```js
measure(G, P1, P2)
```

Measurement between two point variables

### Colored measurement

```js
measure(G, line_a, buff(0, -1), c(black))
```

Measurement with specific color

## Examples

### Measure side a with offset below

```js
measure_a = measure(graph_1, line_a, buff(0, -1), c(black))
```

### Measure side b with offset

```js
measure_b = measure(graph_1, line_b, buff(0, -0.5))
```

### Measure side c with offset

```js
measure_c = measure(graph_1, line_c, buff(0, -0.5))
```

### Hide measurements initially

```js
hide(measure_a, measure_b, measure_c)
```

### Measure between two points directly

```js
measure_1 = measure(graph_1, point_A, point_B, buff(0, 0.5))
```

### Measure extracted edge

```js
edge_measure = measure(graph_1, line(graph_1, item(triangle_1, type(edge), 1), type(segment)), buff(0, -0.5))
```
