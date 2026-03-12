---
title: label
sidebar_label: label
---

# label

Place a text annotation near a point on a 2D graph, with a directional offset to avoid overlapping the point marker. Used for displaying vertex names, point labels, or coordinate annotations.

**Utility:** Label a point with text positioned nearby using buff offset

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container |
| `position` | `at(point_var) \| point_var` | Yes | Point to label. Use at(point_var) preferred, or point_var directly. |
| `text` | `string` | Yes | Label text - typically point name like "A", "P", or coordinates |
| `buff` | `buff(col, row)` | No | Offset from point. Positive col = right, positive row = down. Essential for point labels to avoid overlap. |

## Variants

### Upper-right of point

```
label(G, at(P), "P", buff(0.5, 0.5))
```

Text appears above and to the right of point

### Upper-left of point

```
label(G, at(P), "P", buff(-1, 1))
```

Text appears above and to the left of point

### Lower-left of point

```
label(G, at(P), "Q", buff(-1, -1))
```

Text appears below and to the left of point

### Lower-right of point

```
label(G, at(P), "P", buff(0.5, -0.5))
```

Text appears below and to the right of point

### Direct above point

```
label(G, at(P), "P", buff(0, 1))
```

Text appears directly above point

### Direct below point

```
label(G, at(P), "P", buff(0, -1))
```

Text appears directly below point

### Label without offset (legacy)

```
label(G, P, "A")
```

Label at point with no offset, text may overlap dot

### Label at inline point

```
label(G, point(G, 2, fun(eq, 2)), eq_s, buff(-2))
```

Label at an inline point on a function curve

## Examples

### Label point with upper-right offset

```
point_1 = point(graph_1, -3.1, 1.8)
label_1 = label(graph_1, at(point_1), "A", buff(0.5, 0.5))
```

### Label point P above-left

```
p = point(G, 0.8, fun(eq, 0.8))
label(G, p, "P", buff(-1, 1))
```

### Label point Q below-left

```
q = point(G, 2, fun(eq, 2))
label(G, q, "Q", buff(-1, -1))
```

### Label point with no offset

```
P = point(G, S, 0)
label(G, P, "A")
```

### Label point with no buff, just name

```
label(G, p1, "P")
```

### Label point Q with offset (two graphs)

```
q1 = point(G, q1x, fun(eq, q1x))
label(G, q1, "Q", buff(-2, -1))
```

### Label at function evaluation point with string variable

```
eq_s = "1/x^2"
eq = def(x, eq_s)
label(K, point(K, 2, fun(eq, 2)), eq_s, buff(-2))
```

### Label extracted vertex point from polygon

```
point_A = point(graph_1, item(triangle_1, type(vertex), 1))
label_A = label(graph_1, at(point_A), "A", buff(0.5, 0.5))
```
