---
title: arrow
sidebar_label: arrow
---

# arrow

Draws a curved or straight arrow connecting two shapes or anchor points, with adjustable curvature direction and an optional text label along the path.

**Utility:** Draw animated curved arrows connecting two shapes or anchor points

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `from` | `variable \| corner(var, pos) \| at(var, type(anchor)) \| at(table, row, col)` | Yes | Source endpoint - a shape variable, corner anchor, at() positioned target, or table cell |
| `to` | `variable \| corner(var, pos) \| at(var, type(anchor)) \| at(table, row, col)` | Yes | Destination endpoint - a shape variable, corner anchor, at() positioned target, or table cell |
| `curvature` | `number` | No | Arc curvature in logical units. Positive = clockwise, negative = counter-clockwise, 0 = straight |
| `text` | `string` | No | Text label rendered along the arrow curve path |
| `color` | `c(colorName)` | No | Arrow color - e.g., c(red), c(blue) |
| `strokeWidth` | `s(width)` | No | Arrow stroke width - e.g., s(3), s(5) |

## Variants

### Center to center

```js
arrow(A, B)
```

Arrow from center of shape A to center of shape B

### With curvature

```js
arrow(A, B, 2)
```

Curved arrow with positive (clockwise) arc

### With text label

```js
arrow(A, B, 1, "label")
```

Arrow with text rendered along the curve

### Corner to corner

```js
arrow(corner(A, 4), corner(B, 8))
```

Arrow from right edge of A to left edge of B

### Table cell to shape

```js
arrow(at(T, row, col), P, "text")
```

Arrow from a table cell to a shape with label text

### Positioned anchors

```js
arrow(at(W, type(bottom)), at(X, type(left)), 1.5)
```

Arrow from bottom of W to left side of X with curvature

### With styling

```js
arrow(A, B, -2, c(red), s(5))
```

Styled arrow with negative curvature, red color, thick stroke

### Select to shape

```js
arrow(at(D, 6, 1), at(L, 2), 1)
```

Arrow from a select expression anchor to another expression

## Examples

### Arrow from table cell to a point on graph with label

```js
arrow(at(T, 1, 2), P, "f(x)")
```

### Styled arrow from table cell to point with negative curvature

```js
arrow(at(T, 1, 1), at(P1), -2, c(red), s(5))
```

### Arrow between write expressions with curvature

```js
arrow_1 = arrow(at(write_7, type(bottom)), at(write_8_select_1, type(left)), 1.5)
```

### Arrow from select anchor to print expression

```js
arrow(at(D, 6, 1), at(L, 2), 1)
```

### Simple arrow between two shapes

```js
arrow_1 = arrow(G, M)
```
