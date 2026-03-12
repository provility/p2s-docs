---
title: textupdate
sidebar_label: textupdate
---

# textupdate

Replace the content of a text object with a new string at the same position, fading out the old content. Useful for equation transformations, variable substitutions, and step-by-step simplifications.

**Utility:** Replace text content with new string at same position

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `target` | `variable` | Yes | Reference to write or label object (NOT selections) |
| `newString` | `string` | Yes | New ASCII math content in quotes |
| `buff` | `buff(row, col)` | No | Position offset for new content |

## Variants

### Basic update

```js
textupdate(M, "new content")
```

Update with new string

### With position offset

```js
textupdate(M, "new", buff(0, 1))
```

Update with offset

## Examples

### Update equation during simplification

```js
M = write(at(3, 2), "2x + 3 = 11", type(print))
textupdate(M, "2x = 8")
```

### Update label with new value

```js
L = label(graph_1, at(point_1), "?", buff(0, 0.5))
textupdate(L, "sqrt(a^2-x^2)")
```

### Update derivative step

```js
M = write(at(5, 2), "d/dx[x^3]", type(write))
textupdate(M, "3x^2")
```

### Update with offset for alignment

```js
M = write(at(2, 4), "a = b", type(print))
textupdate(M, "a + c = b + c", buff(0, 0.5))
```
