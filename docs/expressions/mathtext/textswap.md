---
title: textswap
sidebar_label: textswap
---

# textswap

Exchange two text elements with a crossing animation, placing new content at each other's position. Ideal for algebraic transposition, commutative demonstrations, and term rearrangement with sign changes.

**Utility:** Swap two texts with crossing animation and new content

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `dest` | `variable` | Yes | First text object (receives sourceString after swap) |
| `source` | `variable` | Yes | Second text object (receives destString after swap) |
| `destString` | `string` | Yes | New content to place at dest position |
| `sourceString` | `string` | Yes | New content to place at source position |
| `destBuff` | `buff(row, col)` | Yes | Position offset for dest |
| `sourceBuff` | `buff(row, col)` | Yes | Position offset for source |

## Variants

### Basic swap with buffs

```js
textswap(dest, source, "destStr", "srcStr", buff(0, 0), buff(0, 0))
```

Swap with zero offsets

### Swap with different offsets

```js
textswap(dest, source, "d", "s", buff(r1, c1), buff(r2, c2))
```

Swap with independent position adjustments

## Examples

### Move term across equals with sign change (a+b=c becomes a-c=-b)

```js
write_1 = write(at(8.1, 7.5), "a+b=c", type(write))
select_1 = select(write_1, "+b", 1)
select_2 = select(write_1, "c", 1)
text_swap_5 = textswap(select_2, select_1, "-b", "-c", buff(-0.1, 0.6), buff(0, 0))
```

### Swap selected terms with new values

```js
select_10 = select(write_11, "a", 1)
select_11 = select(write_12, "theta", 1)
text_swap_1 = textswap(select_10, select_11, "theta", "a", buff(0, 0), buff(0, 0))
```

### Swap variables in equation

```js
M = write(at(3, 2), "x + y = z", type(print))
X = select(M, "x", 1)
Y = select(M, "y", 1)
textswap(X, Y, "y", "x", buff(0, 0), buff(0, 0))
```

### Transpose with position offsets

```js
M = write(at(4, 4), "2x + 3 = 11", type(print))
left = select(M, "+3", 1)
right = select(M, "11", 1)
textswap(right, left, "11 - 3", "2x", buff(0, 0.3), buff(0, -0.3))
```
