---
title: mcancel
sidebar_label: mcancel
---

# mcancel

Draws a diagonal strikethrough line across a selected text region to indicate algebraic cancellation or elimination, supporting down, up, and X-pattern directions.

**Utility:** Draw a cancel strikethrough line on selected text to show elimination

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `textItem` | `variable (TextItem)` | Yes | A TextItem variable from select() - the target to cancel |
| `direction` | `"u" \| "d" \| "x"` | No | Cancel direction: "u" = up diagonal, "d" = down diagonal (default), "x" = X pattern |
| `color` | `c(colorName)` | No | Strikethrough color - e.g., c(red), c(blue) |
| `strokeWidth` | `s(width)` | No | Strikethrough stroke width - e.g., s(3) |

## Variants

### Default cancel (down diagonal)

```
mcancel(D)
```

Cancel with a down diagonal line

### Up diagonal cancel

```
mcancel(D, "u")
```

Cancel with an up diagonal line (bottom-left to top-right)

### X pattern cancel

```
mcancel(D, "x")
```

Cancel with an X pattern (both diagonals)

### Styled cancel

```
mcancel(D, "u", c(red), s(3))
```

Up diagonal cancel with red color and thick stroke

### Colored cancel

```
mcancel(D, c(blue))
```

Default diagonal cancel with blue color

## Examples

### Cancel the discriminant in a quadratic formula

```
D = select(Q, "b^2 - 4ac", 1)
mcancel_1 = mcancel(D)
```

### Cancel with up diagonal and red color

```
D = select(Q, "b^2 - 4ac", 1)
mcancel_1 = mcancel(D, "u", c(red))
```

### Cancel with X pattern and styling

```
select_1 = select(write_1, "sin^2(x)", 1)
mcancel_1 = mcancel(select_1, "x", c(blue), s(3))
```
