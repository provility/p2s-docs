---
title: label
sidebar_label: label
---

# label

Place a text annotation at the arc midpoint of a geometric angle, with a directional offset into the angle interior for displaying angle names, Greek letters, or degree values.

**Utility:** Label an angle arc with name or measurement using buff offset

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container |
| `position` | `at(angle_var)` | Yes | Angle variable created by angle() expression |
| `text` | `string` | Yes | Angle name or value - e.g., "A", "theta", "30", "alpha" |
| `buff` | `buff(col, row)` | Yes | Offset to position text in the angle's interior. Direction depends on angle orientation. Required for angle labels to avoid overlapping the arc. |

## Variants

### Label angle at top-left vertex (opens down-right)

```js
label(G, at(angle_A), "A", buff(-1.0, 1.0))
```

Angle A at top-left, text offset up and to the left

### Label angle at bottom-left vertex (opens up-right)

```js
label(G, at(angle_B), "B", buff(-1.0, -1.8))
```

Angle B at bottom-left, text offset down and to the left

### Label angle at right vertex (opens left)

```js
label(G, at(angle_C), "C", buff(1.0, -1))
```

Angle C at right, text offset to the right

### Label angle with Greek letter

```js
label(G, at(angle_2), "theta", buff(-0.9, -2))
```

Greek letter theta at angle position

### Label angle with degree value

```js
label(G, at(angle_A), "30", buff(-0.5, 0.5))
```

Numeric degree value at angle position

## Examples

### Label angle A at top-left vertex of triangle

```js
angle_A = angle(graph_1, item(triangle_1, type(angle), 1), 0.8, type(interior))
label_A = label(graph_1, at(angle_A), "A", buff(-1.0, 1.0))
```

### Label angle B at bottom-left vertex

```js
angle_B = angle(graph_1, item(triangle_1, type(angle), 2), 0.8, type(interior))
label_B = label(graph_1, at(angle_B), "B", buff(-1.0, -1.8))
```

### Label angle C at right vertex

```js
angle_C = angle(graph_1, item(triangle_1, type(angle), 3), 0.8, type(interior))
label_C = label(graph_1, at(angle_C), "C", buff(1.0, -1))
```

### Label angle with theta in trig context

```js
angle_2 = angle(graph_1, item(triangle_1, type(angle), 2), 0.8, type(interior))
label_2 = label(graph_1, at(angle_2), "theta", buff(-0.9, -2))
```

### Label angle with numeric degree value (AAS)

```js
angle_A = angle(graph_1, item(triangle_1, type(angle), 1), 0.8, type(interior))
label_A = label(graph_1, at(angle_A), "30", buff(-0.5, 0.5))
```

### Label angle then move text from write selection to it

```js
L = label(graph_1, at(angle_2), "theta", buff(-0.9, -2))
S = select(write_1, "theta", 1)
textmove(S, L)
```
