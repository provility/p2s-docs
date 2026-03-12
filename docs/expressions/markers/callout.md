---
title: callout
sidebar_label: callout
---

# callout

Draw a circle highlight around a text selection with a curved arrow pointing outward to draw attention to specific sub-expressions. Supports configurable anchor direction, arrow length, curvature, color styling, and optional label text.

**Utility:** Circle a text selection with a curved arrow for emphasis

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `target` | `TextItem variable` | Yes | A TextItem variable from select() to circle with callout |
| `corner` | `corner(n)` | No | Anchor position (0=center, 1-8 clockwise from top-left). Default: corner(4) = right |
| `length` | `number` | No | Arrow length in logical units (default: 2) |
| `curvature` | `number` | No | Curve amount in logical units (default: 2) |
| `color` | `c(colorName)` | No | Stroke color - e.g., c(blue), c(red) |
| `strokeWidth` | `s(number)` | No | Stroke width - e.g., s(3) |

## Variants

### Basic callout

```
callout(T)
```

Default callout with arrow pointing right

### With corner anchor

```
callout(T, corner(2))
```

Callout with arrow pointing up from top-center

### With length and curvature

```
callout(T, corner(2), 3, 1.5)
```

Custom arrow length and curvature

### With styling

```
callout(T, corner(2), 3, 1.5, c(blue))
```

Callout with blue color

### Marker syntax with anchor

```
marker(at(target, type(right)), type(callout), 3, 0.3)
```

Unified marker syntax with length and curvature

### Marker with label and fadein

```
marker(at(target, type(right)), type(callout), 3, 0.3, "Note", fadein(5))
```

Marker callout with label text and animation

## Examples

### Callout on discriminant pointing right

```
Q = write(at(6, 4), "x = (-b +- sqrt(b^2 - 4ac)) / (2a)", type(write))
D = select(Q, "b^2 - 4ac", 1)
callout_1 = callout(D)
```

### Callout with corner anchor and custom arrow

```
D = select(write_1, "x^2", 1)
callout_2 = callout(D, corner(2), 3, 1.5, c(blue))
```

### Callout using unified marker syntax (from trig-substitution lesson)

```
select_7 = select(write_15, "sqrt(a^2-x^2)", 1)
marker_1 = marker(at(select_7, type(right)), type(callout), 3, 0.3)
```

### Marker callout with label text and fadein

```
sel = select(write_1, "a+b", 1)
marker_2 = marker(at(sel, type(top)), type(callout), 3, 0.3, "sum", fadein(5))
```
