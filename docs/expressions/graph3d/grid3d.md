---
title: grid3d
sidebar_label: grid3d
---

# grid3d

Styles the color and stroke width of 3D gridlines rendered on coordinate planes.

**Utility:** Style 3D gridline color and stroke width inside axes3d

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `color` | `c(colorName)` | No | Grid color using c() expression - e.g., c(gray), c(blue) |
| `strokeWidth` | `s(width)` | No | Grid stroke width using s() expression - e.g., s(0.5), s(1) |

## Variants

### Color only

```js
grid3d(c(gray))
```

Set gridline color

### Color and stroke width

```js
grid3d(c(gray), s(0.5))
```

Set gridline color and line thickness

## Examples

### Gray gridlines with default width

```js
G = g3d(at(0, 0), 30, 30, axes3d(range3d(range(-5, 5), range(-5, 5), range(-5, 5)), grid3d(c(gray)), "gridlines"))
```

### Blue gridlines with thin stroke

```js
G = g3d(at(5, 5), 20, 20, axes3d(range3d(range(-10, 10), range(-10, 10), range(-5, 5)), grid3d(c(blue), s(0.5)), "gridlines", "lhs"))
```

### Red gridlines with thick stroke in RHS system

```js
G = g3d(at(0, 0), 25, 25, axes3d(range3d(range(-5, 5), range(-5, 5), range(-5, 5)), grid3d(c(red), s(1)), "gridlines", "rhs"))
```
