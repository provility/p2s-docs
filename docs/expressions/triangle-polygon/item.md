---
title: item
sidebar_label: item
---

# item

Extracts an individual edge, vertex, or angle from a polygon or triangle by 1-based index for use in further geometric constructions.

**Utility:** Extract edge, vertex, or angle from polygon by index for further use

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `polygon` | `polygon \| sss \| sas \| asa \| aas \| rect \| square` | Yes | Polygon or triangle variable to extract from |
| `extractType` | `type(edge) \| type(vertex) \| type(angle)` | Yes | Type of component to extract |
| `index` | `number (1-based)` | Yes | Index of component (1, 2, 3 for triangle; 1-4 for rectangle) |

## Variants

### Extract edge

```
item(polygon, type(edge), 1)
```

Extract first edge as line data (start/end points)

### Extract vertex

```
item(polygon, type(vertex), 2)
```

Extract second vertex as point data

### Extract angle

```
item(polygon, type(angle), 1)
```

Extract angle at first vertex for angle()

## Examples

### Create triangle and extract all edges as lines

```
triangle_1 = sas(graph_1, 5, 40, 6, point(graph_1, 0, 0))
```

### Draw first edge (opposite vertex A) as blue line

```
line_a = line(graph_1, item(triangle_1, type(edge), 1), type(segment), c(blue))
```

### Draw second edge as line

```
line_b = line(graph_1, item(triangle_1, type(edge), 2), type(segment), c(blue))
```

### Draw third edge as line

```
line_c = line(graph_1, item(triangle_1, type(edge), 3), type(segment), c(blue))
```

### Extract and draw angle at vertex 1

```
angle_A = angle(graph_1, item(triangle_1, type(angle), 1), 0.8)
```

### Extract and draw angle at vertex 2

```
angle_B = angle(graph_1, item(triangle_1, type(angle), 2), 0.8)
```

### Extract and draw angle at vertex 3

```
angle_C = angle(graph_1, item(triangle_1, type(angle), 3), 0.8)
```

### Label positioned at an angle

```
label_A = label(graph_1, at(angle_A), "A", buff(-1.0, 1.0))
```

### Label positioned at an edge

```
label_a = label(graph_1, at(item(triangle_1, type(edge), 2)), "a", buff(-1.5, 1))
```

### Measure a line extracted from edge

```
measure_a = measure(graph_1, line_a, buff(0, -1), c(black))
```

### Extract vertex and draw as visible point

```
point_A = point(graph_1, item(triangle_1, type(vertex), 1), c(red))
```

### Project a vertex onto a line

```
point_D = project(graph_1, line_c, item(triangle_1, type(vertex), 3))
```
