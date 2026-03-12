---
title: select
sidebar_label: select
---

# select

Extract and target a specific sub-expression within rendered mathematical text by pattern matching with an occurrence index. Returns a reference to the matched term for subsequent manipulation or highlighting.

**Utility:** Extract and target specific portions of math text for manipulation

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `source` | `variable` | Yes | Reference to the math text variable (from write) |
| `pattern` | `string` | Yes | Pattern to match - ASCII math string in quotes |
| `ordinal` | `number` | Yes | 1-based occurrence index (1=first match, 2=second, etc.) |

## Variants

### Select specific occurrence

```
select(M, "pattern", 1)
```

Select first occurrence of pattern

### Filter mode for writeonly/writewithout

```
select("pattern", 1)
```

Pattern filter without source - used inside writeonly/writewithout

## Examples

### Select term from integral for replacement

```
select_1 = select(write_2, "a^2-x^2", 1)
```

### Select variable x in equation

```
select_9 = select(write_7, "x", 1)
```

### Select term from simplified expression

```
select_6 = select(write_13, "a cos(theta)", 1)
```

### Select pattern for correlation highlight

```
select_10 = select(write_11, "a", 1)
```

### Select theta for swap operation

```
select_11 = select(write_12, "theta", 1)
```
