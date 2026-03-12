---
title: "G2D + Table"
sidebar_label: "G2D + Table"
---

# G2D + Table

Operations available when you select a **g2d** and a **table** together.

## How to Use

```
  1. Click on a g2d object to select it
  2. Hold Shift and click on a table object
  3. Right-click to open the context menu
  4. Choose an operation from the menu
```

## Available Operations

| Operation | Description |
|-----------|-------------|
| **Plot as Curve** | Handler for g2d+table selection (cross-container) |
| **Plot as Points** | Plot table data as a smooth curve on the graph |

## Expression Details

**Handler for g2d+table selection (cross-container)**

```
plottable(graphLabel, tableLabel)           - Plot as curve
```

**Plot table data as a smooth curve on the graph**

```
plottable(G, T)
```

**Plot table data as discrete points with labels on the graph**

```
plottable(G, T, 2, type(points))
```
