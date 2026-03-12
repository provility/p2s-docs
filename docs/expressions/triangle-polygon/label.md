---
title: label
sidebar_label: label
---

# label

Places a text annotation at a specified position on the graph, supporting ASCII-to-LaTeX math notation, offset positioning, and rotation.

**Utility:** Add text label at specified position on graph

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container created with g2d() |
| `position` | `at(point) \| at(shape) \| at(item())` | Yes | Position using at() expression (required) |
| `text` | `string` | Yes | Label text in quotes (ASCII math converted to LaTeX) |
| `buff` | `buff(row, col)` | No | Offset from position in logical units |
| `rotation` | `rotation(degrees)` | No | Rotate label text by degrees |
| `renderType` | `type(write) \| type(print)` | No | type(write) for pen animation, type(print) for instant display |

## Variants

### Label at angle

```js
label(G, at(angle_A), "A", buff(-1.0, 1.0))
```

Label positioned at angle with offset

### Label at edge

```js
label(G, at(item(triangle, type(edge), 1)), "a")
```

Label at edge midpoint

### Label at point

```js
label(G, at(point_A), "A", buff(0.5, 0.5))
```

Label near a point with offset

### Rotated label

```js
label(G, at(line), "side", rotation(30))
```

Label rotated to match line angle

### Instant display

```js
label(G, at(P), "text", type(print))
```

Label without pen animation

## Examples

### Label angle A with offset

```js
label_A = label(graph_1, at(angle_A), "A", buff(-1.0, 1.0))
```

### Label angle B with offset

```js
label_B = label(graph_1, at(angle_B), "B", buff(-1.0, -1.8))
```

### Label angle C with offset

```js
label_C = label(graph_1, at(angle_C), "C", buff(1.0, -1))
```

### Label edge (side a) with rotation

```js
label_a = label(graph_1, at(item(triangle_1, type(edge), 2)), "a", buff(-1.5, 1), rotation(26))
```

### Label side c at edge midpoint

```js
label_c = label(graph_1, at(item(triangle_1, type(edge), 1)), "c", buff(0, -0.5))
```

### Label side b with offset

```js
label_b = label(graph_1, at(item(triangle_1, type(edge), 3)), "b", buff(-1.5, -1.5))
```

### Label at height line

```js
label_h = label(graph_1, at(line_height, 3), "h", buff(0, 0.5))
```

### Greek letter label

```js
label_theta = label(graph_1, at(angle_2), "theta", buff(-0.9, -2))
```
