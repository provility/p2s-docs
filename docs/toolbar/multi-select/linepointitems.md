---
title: "Line + Point"
sidebar_label: "Line + Point"
---

# Line + Point

Operations available when you select a **line** and a **point** together.

## How to Use

```
  1. Click on a line object to select it
  2. Hold Shift and click on a point object
  3. Right-click to open the context menu
  4. Choose an operation from the menu
```

## Available Operations

| Operation | Description |
|-----------|-------------|
| **Project** | Handler for line+point selection |
| **Reflect** | Project point onto line (foot of perpendicular) |
| **Perpendicular** | Reflect point across line |
| **Parallel** | Create perpendicular line through point |

## Expression Details

**Project point onto line (foot of perpendicular)**

```
project(G, L, P)
```

**Reflect point across line**

```
reflect(G, L, P)
```

**Create perpendicular line through point**

```
perp(G, L, P, type(line|segment|ray))
```

**Create parallel line through point**

```
pll(G, L, P, type(line|segment|ray))
```
