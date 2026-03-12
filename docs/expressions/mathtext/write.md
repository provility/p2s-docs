---
title: write
sidebar_label: write
---

# write

Render a mathematical expression on the canvas using ASCII math syntax, with either animated pen-tracing or instant KaTeX display. Supports positioning, color, duration, and media association.

**Utility:** Render mathematical text on canvas with optional pen-tracing animation

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `position` | `at(row, col)` | Yes | Position using logical row, col coordinates |
| `content` | `string` | Yes | ASCII math expression in quotes - e.g., "x^2 + y^2", "int sqrt(a^2-x^2) dx" |
| `renderType` | `type(print) \| type(write)` | Yes | type(print) for instant KaTeX, type(write) for animated pen-tracing |
| `media` | `media("name")` | No | Associate audio/video media with the expression |
| `duration` | `t(seconds)` | No | Animation duration in seconds |
| `color` | `c(colorName)` | No | Text color - e.g., c(blue), c(red) |

## Variants

### Animated pen-tracing

```js
write(at(row, col), "content", type(write))
```

Draws expression stroke-by-stroke

### Instant display

```js
write(at(row, col), "content", type(print))
```

Renders instantly using KaTeX

### With media

```js
write(at(row, col), "content", type(write), media("audio-name"))
```

Associates audio/video with the expression

### With duration

```js
write(at(row, col), "content", type(write), t(2))
```

Custom animation duration

### With color

```js
write(at(row, col), "content", type(write), c(blue))
```

Colored text

## Examples

### Display integral with pen animation and media

```js
write_1 = write(at(3.1, 2.2), "int sqrt(a^2-x^2) dx", type(write), media("trig-sub-intro"))
```

### Show substitution equation

```js
write_7 = write(at(8, 3), "x = a sin(theta)", type(write))
```

### Display simplified result

```js
write_13 = write(at(19, 17.5), "= a cos(theta)", type(write))
```

### Show derivative step

```js
write_14 = write(at(8, 11), "=> dx = a cos(theta) d theta", type(write))
```

### Display final integration result

```js
write_16 = write(at(23, 25.8), "= a^2 int cos^2 theta d theta", type(write))
```
