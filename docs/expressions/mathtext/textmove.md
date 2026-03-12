---
title: textmove
sidebar_label: textmove
---

# textmove

Animate moving a text object from its current position to a new destination with a smooth 2-second transition. Supports absolute coordinates, selection-based anchoring, and position offsets.

**Utility:** Animate moving text object to new position

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `destination` | `at(row, col) \| selection` | Yes | Target position or selection as anchor |
| `source` | `variable` | Yes | Write or label object to move |
| `buff` | `buff(row, col)` | No | Position offset from destination |

## Variants

### Move to absolute position

```js
textmove(at(row, col), source)
```

Move source to specified coordinates

### Move to selection position

```js
textmove(selection, source)
```

Move source to selection's position

### With offset

```js
textmove(destination, source, buff(r, c))
```

Move with additional offset

## Examples

### Move equation to new position

```js
M = write(at(2, 2), "x^2 + y^2", type(print))
textmove(at(4, 5), M)
```

### Move label to selection position

```js
L = label(graph_1, at(angle_2), "theta", buff(-0.9, -2))
S = select(write_1, "theta", 1)
textmove(S, L)
```

### Move with offset

```js
M = write(at(3, 3), "result", type(print))
textmove(at(5, 5), M, buff(0.5, 0))
```
