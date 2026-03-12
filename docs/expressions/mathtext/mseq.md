---
title: mseq
sidebar_label: mseq
---

# mseq

Create systems of equations with proper alignment and visual separator lines between groups. Useful for linear systems, optimization constraints, parametric equations, and differential equations with initial conditions.

**Utility:** Display systems of equations with separators

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `equations` | `"equation # label", "---", ...` | Yes | Quoted equations and --- separators |

## Variants

### Two-equation system with labels

```
print(at(row, col), mseq("x + y = 5 # 1", "x - y = 1 # 2"))
```

Simple system with numbered labels

### With separator line

```
print(at(row, col), mseq("objective # 1", "---", "constraint # 2"))
```

Equations separated by horizontal line

## Examples

### Display 2x2 linear system

```
write_1 = print(at(3, 2), mseq("x + y = 5 # 1", "---", "x - y = 1 # 2"))
```

### Show optimization problem

```
write_2 = print(at(4, 3), mseq("maximize: z = 3x + 2y # objective", "---", "x + y <= 10 # constraint 1", "x >= 0 # constraint 2"))
```

### Display parametric equations

```
write_3 = write(at(5, 2), mseq("x = t^2 # 1", "y = 2t # 2", "z = t^3 # 3"))
```

### Show DE with initial condition

```
write_4 = print(at(2, 4), mseq("dy/dx = 2x # ODE", "---", "y(0) = 1 # IC"))
```
