---
title: at (expression-relative)
sidebar_label: at (expression-relative)
---

# at (expression-relative)

Position an element relative to another expression's location using anchor types (top, bottom, left, right) or table cell references (row, col).

**Utility:** Position elements relative to another expression's location

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `expression` | `variable reference \| item() \| select()` | Yes | Reference to an existing expression (point, angle, line, edge, write, select, etc.) |
| `anchorType` | `type(top) \| type(bottom) \| type(left) \| type(right)` | No | Anchor position on the referenced expression (used with arrows and markers) |
| `tableRow` | `number` | No | Row index when referencing a table cell |
| `tableCol` | `number` | No | Column index when referencing a table cell |

## Variants

### Label at a point

```
label(G, at(point_1), "A", buff(0.5, 0.5))
```

Position label at a point with offset

### Label at an angle

```
label(G, at(angle_A), "A", buff(-1.0, 1.0))
```

Position label at an angle vertex

### Label at edge via item()

```
label(G, at(item(triangle, type(edge), 1)), "a", buff(0, 0.5))
```

Position label at edge midpoint extracted from polygon

### Arrow from expression anchor

```
arrow(at(write_1, type(bottom)), at(write_2, type(left)), 1.5)
```

Arrow from bottom of one write to left of another

### Arrow from table cell to point

```
arrow(at(T, 1, 2), P, "f(x)")
```

Arrow from table cell at row 1, col 2 to point P

### Arrow between table cell and point

```
arrow(at(T, 1, 1), at(P1), -2, c(red), s(5))
```

Arrow from table cell to point with curvature and style

### Marker at expression with anchor

```
marker(at(point_1, type(right)), type(surround))
```

Place marker at the right side of a point

### Marker at select with anchor and buff

```
marker(at(select_7, type(right)), type(8), buff(0.5, 0))
```

Place marker at a text selection's right side with offset

### Arrow between select and write

```
arrow(at(D, 6, 1), at(L, 2), 1)
```

Arrow from select position to write with curvature

## Examples

### Label a point with offset

```
label_1 = label(graph_1, at(point_1), "point_1", buff(0.5, 0.5))
```

### Label triangle edge 'a' with rotation

```
label_1 = label(graph_1, at(item(triangle_1, type(edge), 2)), "a", buff(-2, -0.7), rotation(26), type(write))
```

### Label angle theta

```
label_2 = label(graph_1, at(angle_2), "theta", buff(-0.9, -2))
```

### Label triangle edge with question mark

```
label_3 = label(graph_1, at(item(triangle_1, type(edge), 1)), "?", buff(0, 0.5), rotation(0))
```

### Label triangle edge 'x' with offset

```
label_5 = label(graph_1, at(item(triangle_1, type(edge), 3)), "x", buff(-0.2, -1.1), rotation(0))
```

### Arrow connecting two write expressions

```
arrow_1 = arrow(at(write_7, type(bottom)), at(write_8_select_1, type(left)), 1.5)
```

### Arrow from table cell to a point on graph

```
arrow(at(T, 1, 2), P, "f(x)")
```

### Arrow from table cell to point with style

```
arrow(at(T, 1, 1), at(P1), -2, c(red), s(5))
```

### Marker highlighting a point

```
marker_1 = marker(at(point_1, type(right)), type(surround))
```

### Marker at a text selection with offset

```
marker_1 = marker(at(select_7, type(right)), type(8), buff(0.5, 0))
```

### Label Q on a graph point with offset

```
label(G, q1, "Q", buff(-2, -1))
```
