---
title: p
sidebar_label: p
---

# p

Inline modifier that controls the number of decimal places displayed for computed numeric values.

**Utility:** Set decimal precision for numeric display in tables

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `precision` | `integer` | Yes | Number of decimal places to display - non-negative integer, e.g., 0, 2, 4 |

## Variants

### Integer precision

```
p(0)
```

Display whole numbers only, no decimal places

### Standard precision

```
p(2)
```

Display two decimal places (default)

### High precision

```
p(4)
```

Display four decimal places for detailed values

### Inside table expression

```
table(at(1, 3), "x", "x^2", range(1, 2, 3, 4, 5), p(3))
```

Table with three decimal places of precision

## Examples

### Table with high precision values

```
table_1 = table(at(2, 5), "x", "sin(x)", range(0, 0.5, 1, 1.5, 2), p(4))
```

### Table with integer-only output

```
table_2 = table(at(2, 5), "x", "x^2", range(1, 2, 3, 4, 5), p(0))
```
