---
title: underbrace
sidebar_label: underbrace
---

# underbrace

Draws a curly brace below a selected text region to group or annotate mathematical terms from underneath.

**Utility:** Draw a curly brace below selected text to annotate or group terms

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `textItem` | `variable (TextItem)` | Yes | A TextItem variable from select() - the target to place the brace below |
| `buffer` | `number` | No | Vertical distance from text to brace (default 5) |
| `color` | `c(colorName)` | No | Brace color - e.g., c(blue), c(red) |
| `strokeWidth` | `s(width)` | No | Brace stroke width - e.g., s(3) |

## Variants

### Basic underbrace

```js
underbrace(D)
```

Draw a curly brace below TextItem D with default buffer

### With buffer

```js
underbrace(D, -10)
```

Draw a curly brace with custom vertical buffer

### With color

```js
underbrace(D, c(blue))
```

Draw a blue curly brace below the text

### With buffer and styling

```js
underbrace(D, 10, c(red), s(3))
```

Custom buffer with red color and thick stroke

## Examples

### Underbrace the denominator in a formula

```js
D = select(Q, "2a", 1)
underbrace_1 = underbrace(D)
```

### Blue underbrace with custom buffer

```js
select_1 = select(write_1, "a^2 cos^2(theta)", 1)
underbrace_1 = underbrace(select_1, 10, c(blue))
```

### Styled underbrace under a group of terms

```js
D = select(Q, "b^2 - 4ac", 1)
underbrace_1 = underbrace(D, c(red), s(3))
```
