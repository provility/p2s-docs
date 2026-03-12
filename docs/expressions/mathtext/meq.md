---
title: meq
sidebar_label: meq
---

# meq

Create vertically aligned multi-line equation steps for mathematical derivations and proofs. Each line supports an optional label after a # separator for step annotations.

**Utility:** Display aligned multi-step equations with optional labels

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `lines` | `"equation # label", ...` | Yes | Quoted equation strings, each optionally with # label suffix |

## Variants

### Basic equation steps with labels

```js
print(at(row, col), meq("x^2 = 4 # 1", "x = pm 2 # 2"))
```

Two-line equation with numbered labels

### Animated reveal

```js
write(at(row, col), meq("line1", "line2"))
```

Animate each line sequentially

### Positioned relative to shape

```js
print(at(shape, buff(col, row)), meq("eq1", "eq2"))
```

Position relative to shape with offset

## Examples

### Solve quadratic equation showing each step

```js
write_1 = print(at(4, 4), meq("x^2 = 4 # 1", "x = pm 2 # 2"))
```

### Show algebraic derivation with labels

```js
write_2 = write(at(3, 2), meq("2x + 5 = 11 # given", "2x = 6 # subtract 5", "x = 3 # divide by 2"))
```

### Display trig identity verification

```js
write_3 = print(at(5, 3), meq("sin^2(x) + cos^2(x) # LHS", "= 1 # identity"))
```

### Show integration steps

```js
write_4 = write(at(6, 2), meq("int 2x dx # given", "= x^2 + C # power rule"))
```
