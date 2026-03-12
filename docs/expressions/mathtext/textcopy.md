---
title: textcopy
sidebar_label: textcopy
---

# textcopy

Animate copying content from a source text object to a destination position, preserving both originals. A clone moves from source to destination over 2 seconds.

**Utility:** Copy content from source to target position, target stays visible

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `target` | `variable` | Yes | Destination text object or position variable |
| `source` | `variable` | Yes | Source text object variable (NOT string literals) |
| `buff` | `buff(row, col)` | No | Position offset for copied content |

## Variants

### Basic copy

```js
textcopy(target, source)
```

Copy source content to target position

### With offset

```js
textcopy(target, source, buff(row, col))
```

Copy with position adjustment

## Examples

### Copy from writewithout selection to graph label

```js
write_2 = writewithout(at(12.4, 7.8), "sqrt(x^2 + 1) / (a + b) = x^2+1", select("x^2", 2), type(write), c(red), fc(yellow))
graph_1 = g2d(at(5.1, 27.5), 7.4, 12.2, range(-5, 5), range(-5, 5))
point_1 = point(graph_1, 2, 1)
label_1 = label(graph_1, at(point_1), "A", buff(0.5, 0.5))
text_arrange_1 = textcopy(write_2_select_1, label_1)
```

### Copy selected term to placeholder

```js
write_17 = write(at(23.7, 14.4), "#######", type(write))
select_6 = select(write_13, "a cos(theta)", 1)
text_copy_1 = textcopy(write_17, select_6, buff(0.5, -0.5))
```

### Copy selection to auto-generated slot

```js
select_8 = select(write_14, "a cos(theta) d theta", 1)
text_copy_2 = textcopy(write_15_select_2, select_8)
```

### Copy label content to new position

```js
L1 = label(G, 2, 2, "alpha")
L2 = label(G, 4, 4, "")
textcopy(L2, L1)
```
