---
title: writewithout
sidebar_label: writewithout
---

# writewithout

Render a mathematical expression while hiding selected portions as invisible phantom placeholders that reserve layout space. Ideal for fill-in-the-blank exercises and staged reveal sequences in derivations.

**Utility:** Render expression hiding selected portions as phantom placeholders

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `position` | `at(row, col)` | Yes | Position using logical row, col coordinates |
| `content` | `string` | Yes | Full ASCII math expression including terms to hide |
| `filters` | `select("pattern", index), ...` | Yes | One or more select filters specifying which terms to hide |
| `renderType` | `type(write) \| type(print)` | Yes | type(write) for animated, type(print) for instant |
| `duration` | `t(seconds)` | No | Animation duration |

## Variants

### Hide single term

```
writewithout(at(row, col), "expression", select("term", 1), type(write))
```

Display expression with one term hidden

### Hide multiple terms

```
writewithout(at(row, col), "expr", select("t1", 1), select("t2", 1), type(write))
```

Hide multiple terms as phantoms

### With duration

```
writewithout(at(row, col), "expr", select("term", 1), type(write), t(1))
```

Custom animation timing

## Examples

### Hide second occurrence of x^2 with color and font styling

```
write_2 = writewithout(at(12.4, 7.8), "sqrt(x^2 + 1) / (a + b) = x^2+1", select("x^2", 2), type(write), c(red), fc(yellow))
```

### Hide second occurrence then reveal with textreveal

```
writewithout_1 = writewithout(at(21.4, 14.2), "(a+x^2 + 1) / (x^2 + 1)", select("x^2 + 1", 2), type(write), f(48))
text_reveal_1 = textreveal(writewithout_1_select_1, buff(-0.4, -0.2), notes("hello world"))
```

### Show substitution hiding the substituted term

```
write_8 = writewithout(at(11, 2.5), "sqrt(a^2-x^2) = sqrt(a^2-a^2 sin^2(theta))", select("a^2 sin^2(theta)", 1), type(write), t(1))
```

### Hide multiple terms in expanded integral

```
write_15 = writewithout(at(23.4, 3.2), "int sqrt(a^2-x^2) dx = int a cos(theta) a cos(theta) d theta", select("a cos(theta)", 1), select("a cos(theta) d theta", 1), type(write))
```

### Create fill-in-blank for quadratic solution

```
writewithout(at(3, 2), "x = (-b pm sqrt(b^2-4ac))/(2a)", select("b^2-4ac", 1), type(write))
```
