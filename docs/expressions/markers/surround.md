---
title: surround
sidebar_label: surround
---

# surround

Draw a rectangular highlight box around a selected sub-expression to visually emphasize key terms, discriminants, or results in mathematical notation. Supports custom stroke color and width.

**Utility:** Draw a rectangular highlight box around a text selection

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `target` | `TextItem variable` | Yes | A TextItem variable from select() to surround with a rectangle |
| `color` | `c(colorName)` | No | Stroke color for the rectangle - e.g., c(red), c(blue) |
| `strokeWidth` | `s(number)` | No | Stroke width for the rectangle border - e.g., s(3) |

## Variants

### Basic surround

```js
surround(T)
```

Draw default rectangle around text item T

### Colored surround

```js
surround(T, c(blue))
```

Blue rectangle around text item

### Styled surround

```js
surround(T, c(red), s(3))
```

Red rectangle with custom stroke width

### Marker syntax

```js
marker(at(target, type(right)), type(surround))
```

Unified marker syntax with anchor position

### Marker with fadein

```js
marker(at(target, type(right)), type(surround), fadein(5))
```

Surround via marker with fade-in animation

## Examples

### Highlight discriminant in quadratic formula

```js
Q = write(at(6, 4), "x = (-b +- sqrt(b^2 - 4ac)) / (2a)", type(write))
D = select(Q, "b^2 - 4ac", 1)
surround_1 = surround(D)
```

### Surround with red color and thick border

```js
D = select(write_1, "x^2", 1)
surround_2 = surround(D, c(red), s(3))
```

### Surround a point label using marker syntax (from label-markers lesson)

```js
point_1 = point(graph_1, -3.1, 1.8)
marker_1 = marker(at(point_1, type(right)), type(surround))
```

### Highlight a selected sub-expression with blue

```js
select_1 = select(write_1, "a+b", 1)
surround_3 = surround(select_1, c(blue))
```
