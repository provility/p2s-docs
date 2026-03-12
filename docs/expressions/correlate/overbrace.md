---
title: overbrace
sidebar_label: overbrace
---

# overbrace

Draws a curly brace above a selected text region to group or annotate mathematical terms from above.

**Utility:** Draw a curly brace above selected text to annotate or group terms

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `textItem` | `variable (TextItem)` | Yes | A TextItem variable from select() - the target to place the brace above |
| `buffer` | `number` | No | Vertical distance from text to brace (default 5) |
| `color` | `c(colorName)` | No | Brace color - e.g., c(blue), c(red) |
| `strokeWidth` | `s(width)` | No | Brace stroke width - e.g., s(3) |

## Variants

### Basic overbrace

```
overbrace(D)
```

Draw a curly brace above TextItem D with default buffer

### With buffer

```
overbrace(D, 10)
```

Draw a curly brace with custom vertical buffer

### With color

```
overbrace(D, c(blue))
```

Draw a blue curly brace above the text

### With buffer and styling

```
overbrace(D, 10, c(red), s(3))
```

Custom buffer with red color and thick stroke

## Examples

### Overbrace the discriminant in a formula

```
D = select(Q, "b^2 - 4ac", 1)
overbrace_1 = overbrace(D)
```

### Blue overbrace with custom buffer

```
select_1 = select(write_1, "a cos(theta)", 1)
overbrace_1 = overbrace(select_1, 10, c(blue))
```

### Styled overbrace over a group of terms

```
D = select(Q, "2a", 1)
overbrace_1 = overbrace(D, c(red), s(3))
```
