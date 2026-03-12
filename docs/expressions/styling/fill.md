---
title: f
sidebar_label: f
---

# f

Inline modifier that sets the font size in pixels for text-rendering expressions. Common values range from 12 (small) to 48 (very large).

**Utility:** Set font size on text expressions using inline modifier

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `size` | `number` | Yes | Font size in pixels - positive number, e.g., 16, 24, 36, 48 |

## Variants

### Small text

```
f(16)
```

Small font size for compact text

### Medium text

```
f(24)
```

Medium font size for normal text

### Large text

```
f(36)
```

Large font size for headings

### Very large text

```
f(48)
```

Very large font size for titles

### Inside write expression

```
writewithout(at(21, 14), "(a+x^2 + 1) / (x^2 + 1)", select("x^2 + 1", 2), type(write), f(48))
```

Large font size applied to a writewithout expression

## Examples

### Table with custom font size

```
table_1 = table(at(4, 26), "x", "(x-1)/(x^2-1)", range(0, 0.2, 0.5, 0.7, 0.8, 0.9, 0.99, 0.999, 1, 1.1, 1.2, 2), f(16))
```

### Write expression with large font

```
writewithout_1 = writewithout(at(21.4, 14.2), "(a+x^2 + 1) / (x^2 + 1)", select("x^2 + 1", 2), type(write), f(48))
```
