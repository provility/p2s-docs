---
title: buff
sidebar_label: buff
---

# buff

Apply a horizontal and vertical offset to nudge an element from its anchor position without changing the logical attachment point.

**Utility:** Offset element position by col/row amount in logical units

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `col` | `number` | Yes | Horizontal offset in logical units (positive = right, negative = left) |
| `row` | `number` | No | Vertical offset in logical units (positive = down, negative = up). If omitted, col value is used as a single directional offset. |

## Variants

### Two-argument offset

```js
buff(col, row)
```

Offset by col horizontally and row vertically

### Single-argument offset

```js
buff(value)
```

Single directional offset (context-dependent direction)

### Label with buff

```js
label(G, at(point), "A", buff(0.5, 0.5))
```

Label offset right and down from point

### Measure with buff

```js
measure(G, p1, p2, "", buff(1.7, 1))
```

Measurement line offset from points

### Marker with buff

```js
marker(at(select, type(right)), type(8), buff(0.5, 0))
```

Marker offset from anchor

### Trace with buff

```js
trace(G, V1, type(angle), V2, buff(-6, 0))
```

Trace label offset from default position

### Tangent with buff

```js
tangent(G, f, x, buff(0.3))
```

Single-value buff for tangent rendering offset

### Textswap with buff pairs

```js
textswap(sel1, sel2, "new1", "new2", buff(-0.1, 0.6), buff(0, 0))
```

Each swapped selection gets its own buff offset

### Textreplace with buff

```js
textreplace(label, select, buff(0, -2), type(replace))
```

Replacement text offset

### Textcopy with buff

```js
textcopy(write, select, buff(0.5, -0.5))
```

Copied text offset from source

### Textreveal with buff

```js
textreveal(select, buff(-0.4, -0.2), notes("text"))
```

Revealed text offset

### Interval with buff

```js
interval(nl, 2, 6, type(closed), buff(-19))
```

Single-value buff for interval positioning

### Trace limit with buff

```js
trace(G, plot, type(limit), 1, buff(-1.6, -30))
```

Trace limit label offset

## Examples

### Label top-right of a point

```js
label_1 = label(graph_1, at(point_1), "A", buff(0.5, 0.5))
```

### Label left and up from an angle

```js
label_2 = label(graph_1, at(angle_2), "theta", buff(-0.9, -2))
```

### Label on rotated edge with offset

```js
label_1 = label(graph_1, at(item(triangle_1, type(edge), 2)), "a", buff(-2, -0.7), rotation(26), type(write))
```

### Label above an edge

```js
label_3 = label(graph_1, at(item(triangle_1, type(edge), 1)), "?", buff(0, 0.5), rotation(0))
```

### Label bottom-left with negative offsets

```js
label_5 = label(graph_1, at(item(triangle_1, type(edge), 3)), "x", buff(-0.2, -1.1), rotation(0))
```

### Measurement offset from points

```js
measure_1 = measure(graph_1, point_3, point_4, "", buff(1.7, 1))
```

### Label Q to the left and up

```js
label(G, q1, "Q", buff(-2, -1))
```

### Marker offset from selection

```js
marker_1 = marker(at(select_7, type(right)), type(8), buff(0.5, 0))
```

### Trace label offset for angle readout

```js
trace(G, V1, type(angle), V2, buff(-6, 0))
```

### Single-value buff on tangent

```js
t = tangent(G, f, x, buff(0.3))
```

### Label with single-value buff

```js
label(K, point(K, 2, fun(eq, 2)), eq_s, buff(-2))
```

### Textreveal with buff offset

```js
text_reveal_1 = textreveal(writewithout_1_select_1, buff(-0.4, -0.2), notes("hello world"))
```

### Textswap with paired buff offsets

```js
text_swap_1 = textswap(select_10, select_11, "theta", "a", buff(0, 0), buff(0, 0))
```

### Textcopy with buff offset

```js
text_replace_8 = textcopy(write_17, select_6, buff(0.5, -0.5))
```

### Trace conics focus with buff

```js
trace_1 = trace(graph_2, parabola_1, type(focus), buff(-1, -1))
```
