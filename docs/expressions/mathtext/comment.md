---
title: comment
sidebar_label: comment
---

# comment

Display a temporary positioned annotation with KaTeX math rendering that appears for a configurable duration. Supports anchor-based, absolute, or logical positioning with color, font size, and background styling.

**Utility:** Display positioned annotation comments with optional styling

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `position` | `at(...)` | Yes | Position using at() - can reference shapes, anchor points, or absolute coordinates |
| `text` | `string` | Yes | Comment text in quotes - supports ASCII math syntax |
| `duration` | `t(seconds)` | No | Display duration in seconds (default 2) |
| `color` | `c(colorName)` | No | Text color - e.g., c(blue), c(gray) |
| `fontSize` | `f(size)` | No | Font size in pixels - e.g., f(24) |
| `fillColor` | `fc(colorName)` | No | Background fill color |
| `fillOpacity` | `fo(value)` | No | Background opacity (0-1) |

## Variants

### Center of shape

```js
comment(at(M), "text")
```

Comment at center of shape M

### Shape edge (anchor point)

```js
comment(at(M, 4), "text")
```

Comment at right edge of M (anchor 4)

### With buffer offset

```js
comment(at(M, 4, buff(0.5)), "text")
```

Comment at right edge + 0.5 unit offset

### Two-axis buffer

```js
comment(at(M, 6, buff(0, 0.5)), "text")
```

Comment below shape with vertical offset

### Absolute position

```js
comment(at(5, 3), "text")
```

Comment at row 5, col 3

### Corner position type

```js
comment(at(M, type(topleft)), "text")
```

Comment at top-left corner of M

### With styling

```js
comment(at(M, 4), "text", c(blue), f(24))
```

Colored comment with custom font size

### Custom duration

```js
comment(at(M, 4), "text", t(3))
```

Comment visible for 3 seconds

## Examples

### Annotate equation with theorem name

```js
M = write(at(1, 1), "x^2 + y^2 = r^2", type(print))
comment(at(M, 4, buff(0.5)), "Pythagorean theorem")
```

### Add note below graph with gray color

```js
G = g2d(1, 1, 6, 6)
comment(at(G, 6, buff(0, 0.3)), "Figure 1: Parabola", c(gray))
```

### Explain step in derivation

```js
step_1 = write(at(3, 2), "d/dx(x^2) = 2x", type(write))
comment(at(step_1, 4, buff(1)), "Power rule", c(blue), t(3))
```

### Temporary hint at absolute position

```js
comment(at(10, 5), "Remember: sin^2 + cos^2 = 1", c(green), t(4))
```

### Corner annotation with background

```js
box = rect(2, 2, 8, 6)
comment(at(box, type(topright), buff(0.2)), "Area = l times w", fc(yellow), fo(0.3))
```
