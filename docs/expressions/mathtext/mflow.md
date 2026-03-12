---
title: mflow
sidebar_label: mflow
---

# mflow

Create flow-style mathematical derivations with visual connectors (arrow, implies, iff, therefore) between steps. Ideal for logical deduction chains, limit evaluations, and expression transformation sequences.

**Utility:** Display flow-style derivations with visual connectors

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `steps` | `"step # connector", ...` | Yes | Quoted step strings with optional # connector (arrow, implies, iff, therefore) |

## Variants

### With arrow connectors

```js
print(at(row, col), mflow("x", "x+2 # arrow", "3(x+2) # implies"))
```

Steps connected with arrows and implies symbols

### Animated flow

```js
write(at(row, col), mflow("step1", "step2 # arrow"))
```

Animate steps sequentially

## Examples

### Show algebraic expression transformation

```js
write_1 = print(at(3, 2), mflow("x", "x+2 # arrow", "3(x+2) # implies"))
```

### Display logical deduction chain

```js
write_2 = print(at(4, 3), mflow("x > 0 # implies", "x^2 > 0 # therefore", "sqrt(x^2) = x"))
```

### Show limit evaluation flow

```js
write_3 = write(at(5, 2), mflow("lim_(x->2) (x^2-4)/(x-2) # arrow", "lim_(x->2) (x+2) # arrow", "4"))
```

### Demonstrate equivalence

```js
write_4 = print(at(2, 4), mflow("x + 5 = 10 # iff", "x = 5"))
```
