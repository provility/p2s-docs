---
title: textreveal
sidebar_label: textreveal
---

# textreveal

Animate revealing a previously hidden text selection at its current position using pen-tracing or fade-in animation. Useful for progressive reveal sequences in mathematical derivations.

**Utility:** Animate revealing selected text portions at their position

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `selection` | `variable` | Yes | Reference to a select() result |
| `buff` | `buff(row, col)` | No | Position offset in logical units |

## Variants

### Basic reveal

```
textreveal(selectVar)
```

Reveal selection at its original position

### With position offset

```
textreveal(selectVar, buff(0, 1))
```

Reveal with offset

## Examples

### Reveal hidden selection from writewithout with notes

```
writewithout_1 = writewithout(at(21.4, 14.2), "(a+x^2 + 1) / (x^2 + 1)", select("x^2 + 1", 2), type(write), f(48))
text_reveal_1 = textreveal(writewithout_1_select_1, buff(-0.4, -0.2), notes("hello world"))
```

### Reveal hidden answer in equation

```
M = write(at(3, 2), "x = 5", type(print))
answer = select(M, "5", 1)
hide(answer)
textreveal(answer)
```

### Reveal derivative result

```
M = write(at(4, 3), "f'(x) = 2x", type(write))
result = select(M, "2x", 1)
hide(result)
textreveal(result)
```

### Reveal with offset

```
M = write(at(5, 2), "a^2 + b^2 = c^2", type(print))
rhs = select(M, "c^2", 1)
textreveal(rhs, buff(0, 0.5))
```
