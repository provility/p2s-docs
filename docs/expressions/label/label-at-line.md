---
title: label
sidebar_label: label
---

# label

Place a text annotation at the midpoint of a line segment or polygon edge, with optional rotation to match the edge slope and perpendicular offset to avoid overlap.

**Utility:** Label a line segment or polygon edge with text at its midpoint

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container |
| `position` | `at(item(polygon, type(edge), N)) \| at(line_var)` | Yes | Edge midpoint via item() extraction, or line variable |
| `text` | `string` | Yes | Label text - typically side name (a, b, c) or measurement |
| `buff` | `buff(col, row)` | No | Offset from edge midpoint to avoid overlapping the line |
| `rotation` | `rotation(degrees)` | No | Angle to rotate text. Match the edge slope, or use rotation(0) for horizontal. |

## Variants

### Label edge with rotation matching slope

```
label(G, at(item(tri, type(edge), 2)), "a", buff(-2, -0.7), rotation(26))
```

Label angled edge with text rotated to match

### Label horizontal edge below

```
label(G, at(item(tri, type(edge), 1)), "c", buff(0, -0.5))
```

Label base edge with text below

### Label horizontal edge above

```
label(G, at(item(tri, type(edge), 1)), "c", buff(0, 0.5))
```

Label base edge with text above

### Label vertical side to the left

```
label(G, at(item(tri, type(edge), 3)), "b", buff(-1.5, -1.5))
```

Label vertical edge with text offset to the left

### Force horizontal text on angled edge

```
label(G, at(item(tri, type(edge), 3)), "x", buff(-0.2, -1.1), rotation(0))
```

Label angled edge but keep text horizontal

### Label at standalone line

```
label(G, at(line_height), "h", buff(0, 0.5))
```

Label at a standalone line variable

### Label line with animated pen

```
label(G, at(item(tri, type(edge), 2)), "a", buff(-2, -0.7), rotation(26), type(write))
```

Edge label with explicit pen-tracing animation

## Examples

### Label hypotenuse 'a' with rotation matching slope

```
label_1 = label(graph_1, at(item(triangle_1, type(edge), 2)), "a", buff(-2, -0.7), rotation(26), type(write))
```

### Label base edge 'c' below midpoint

```
label_c = label(graph_1, at(item(triangle_1, type(edge), 1)), "c", buff(0, -0.5))
```

### Label third side 'b' offset left

```
label_b = label(graph_1, at(item(triangle_1, type(edge), 3)), "b", buff(-1.5, -1.5))
```

### Label edge with question mark placeholder

```
label_3 = label(graph_1, at(item(triangle_1, type(edge), 1)), "?", buff(0, 0.5), rotation(0))
```

### Label vertical side 'x' with horizontal text

```
label_5 = label(graph_1, at(item(triangle_1, type(edge), 3)), "x", buff(-0.2, -1.1), rotation(0))
```

### Label a height line

```
label_h = label(graph_1, at(line_height), "h", buff(0, 0.5))
```

### Label edge then update via textreplace from selection

```
label_3 = label(graph_1, at(item(triangle_1, type(edge), 1)), "?", buff(0, 0.5), rotation(0))
select_1 = select(write_2, "a^2-x^2", 1)
text_replace_6 = textreplace(label_3, select_1, buff(0, -2), type(replace))
```
