---
title: correlate
sidebar_label: correlate
---

# correlate

Groups two or more shapes under a shared visual annotation such as a rectangle, circle, strikethrough, brace, or underline to visually link related terms.

**Utility:** Group multiple shapes with a shared visual annotation (surround, circle, cancel, brace, underline)

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `shapes` | `variable, variable, ...` | Yes | Two or more shape variable references to correlate together |
| `annotationType` | `type(surround) \| type(circle) \| type(mcancel) \| type(overbrace) \| type(underbrace) \| type(underline)` | Yes | Visual annotation style to apply across the grouped shapes |

## Variants

### Surround rectangle

```
correlate(A, B, type(surround))
```

Draw a rectangle around the group of shapes

### Circle annotation

```
correlate(A, B, type(circle))
```

Draw an ellipse around the group of shapes

### Cancel strikethrough

```
correlate(A, B, type(mcancel))
```

Draw a cancel line through the group of shapes

### Overbrace

```
correlate(A, B, type(overbrace))
```

Draw a curly brace above the group of shapes

### Underbrace

```
correlate(A, B, type(underbrace))
```

Draw a curly brace below the group of shapes

### Underline

```
correlate(A, B, type(underline))
```

Draw a line underneath the group of shapes

### Multiple shapes

```
correlate(A, B, C, type(surround))
```

Correlate three or more shapes together

## Examples

### Circle matching variables in a trig substitution

```
correlate_1 = correlate(select_9, label_5, type(circle))
```

### Surround two related terms

```
correlate_1 = correlate(select_1, select_2, type(surround))
```

### Underbrace a group of expressions

```
correlate_1 = correlate(write_1, write_2, type(underbrace))
```
