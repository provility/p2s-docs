---
title: label
sidebar_label: label
---

# label

Add a text annotation to any position on a 2D graph, supporting plain text, LaTeX math, Greek letters, dynamic variable substitution, and computed expressions. Positioning supports anchoring at graph objects or absolute coordinates, with optional offset and rotation for precise placement.

**Utility:** Add text label at specified position on a 2D graph

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container created with g2d() |
| `position` | `at(point) \| at(angle) \| at(item()) \| at(x, y) \| point \| x, y` | Yes | Position using at() expression or direct point/coordinate reference |
| `text` | `string` | Yes | Label text in quotes. ASCII math auto-converts to LaTeX. Use :var for variable substitution, :\{expr\} for computed values. |
| `buff` | `buff(col, row)` | No | Offset from anchor position in logical units. Positive col = right, positive row = down. |
| `rotation` | `rotation(degrees)` | No | Rotate label text by given degrees |
| `renderType` | `type(write) \| type(print)` | No | type(write) for animated pen-tracing (default), type(print) for instant KaTeX display |

## Variants

### Label at point with at()

```
label(G, at(P), "A", buff(0.5, 0.5))
```

Label near a named point using at() positioning

### Label at point (legacy)

```
label(G, P, "A")
```

Label at point variable without at() wrapper

### Label at coordinates with at()

```
label(G, at(3, 4), "Point")
```

Label at specific graph coordinates

### Label at raw coordinates (legacy)

```
label(G, 3.2, 4.2, "A")
```

Label at x, y coordinates without at() wrapper

### Label at angle

```
label(G, at(angle_A), "A", buff(-1.0, 1.0))
```

Label positioned at angle arc midpoint with offset

### Label at edge via item()

```
label(G, at(item(triangle_1, type(edge), 2)), "a", buff(-1.5, 1))
```

Label at edge midpoint extracted from polygon

### Label with variable value

```
label(G, at(P), ":x")
```

Display current value of variable x

### Label with computed expression

```
label(G, at(P), ":{a*b}")
```

Display result of computed math expression

### Label with formatted value

```
label(G, at(P), ":x:.2f")
```

Display variable with 2 decimal places

### LaTeX label

```
label(G, at(P), "\\frac{a}{b}")
```

Label with LaTeX-formatted math

### Rotated label

```
label(G, at(line_1), "side", rotation(30))
```

Label rotated to match a line angle

### Instant display label

```
label(G, at(P), "text", type(print))
```

Label renders instantly without pen animation

### Label at inline point

```
label(G, point(G, 2, fun(eq, 2)), "1/x^2", buff(-2))
```

Label at inline point expression for function annotation

## Examples

### Label a point with name

```
label_1 = label(graph_1, at(point_1), "A", buff(0.5, 0.5))
```

### Label a point (legacy syntax)

```
label(G, P, "A")
```

### Label point with no assignment

```
label(G, p, "P", buff(-1, 1))
```

### Label at angle with Greek letter

```
label_2 = label(graph_1, at(angle_2), "theta", buff(-0.9, -2))
```

### Label triangle edge with rotation

```
label_1 = label(graph_1, at(item(triangle_1, type(edge), 2)), "a", buff(-2, -0.7), rotation(26), type(write))
```

### Label triangle edge (horizontal bottom)

```
label_3 = label(graph_1, at(item(triangle_1, type(edge), 1)), "?", buff(0, 0.5), rotation(0))
```

### Label triangle edge (vertical side)

```
label_5 = label(graph_1, at(item(triangle_1, type(edge), 3)), "x", buff(-0.2, -1.1), rotation(0))
```

### Label at solved point on graph

```
label(G, P, "A")
```

### Label at function evaluation point

```
label(K, point(K, 2, fun(eq, 2)), eq_s, buff(-2))
```

### Label with dynamic variable

```
label(G, at(A), "x = :x")
```

### Label with computed area expression

```
label(G, at(A), "Area = :{w*h}")
```

### Label used as textcopy target

```
label_1 = label(graph_1, at(point_1), "A", buff(0.5, 0.5))
text_arrange_1 = textcopy(write_2_select_1, label_1)
```

### Label updated via textupdate

```
L = label(graph_1, at(point_1), "?", buff(0, 0.5))
textupdate(L, "sqrt(a^2-x^2)")
```

### Label content moved via textmove from selection

```
L = label(graph_1, at(angle_2), "theta", buff(-0.9, -2))
S = select(write_1, "theta", 1)
textmove(S, L)
```
