---
title: surround
sidebar_label: surround
---

# surround

Draws a rectangular border around a selected text region to visually highlight or emphasize specific terms in an expression.

**Utility:** Draw a rectangle border around a selected text region to highlight it

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `textItem` | `variable (TextItem)` | Yes | A TextItem variable from select() or similar - the target to surround |
| `color` | `c(colorName)` | No | Border color - e.g., c(red), c(blue) |
| `strokeWidth` | `s(width)` | No | Border stroke width - e.g., s(3) |

## Variants

### Basic surround

```js
surround(D)
```

Draw a default rectangle around TextItem D

### Colored surround

```js
surround(D, c(blue))
```

Draw a blue rectangle around TextItem D

### Styled surround

```js
surround(D, c(red), s(3))
```

Draw a red rectangle with stroke width 3

## Examples

### Highlight discriminant in quadratic formula

```js
Q = write(at(6, 4), "x = frac(-b pm sqrt(b^2 - 4ac))(2a)", type(print))
D = select(Q, "b^2 - 4ac", 1)
surround_1 = surround(D)
```

### Surround with red color and thick stroke

```js
D = select(Q, "4ac", 1)
surround_1 = surround(D, c(red), s(3))
```

### Surround a selected term in blue

```js
select_1 = select(write_1, "x^2", 1)
surround_1 = surround(select_1, c(blue))
```
