---
title: "Vector + Vector"
sidebar_label: "Vector + Vector"
---

# Vector + Vector

Operations available when you select a **vector** and a **vector** together.

## How to Use

```
  1. Click on a vector object to select it
  2. Hold Shift and click on a vector object
  3. Right-click to open the context menu
  4. Choose an operation from the menu
```

## Available Operations

| Operation | Description |
|-----------|-------------|
| **Sum (A + B)** | Handler for two-vector selection (2D) |
| **at** | Vector sum using vecsum expression |
| **Difference (A - B)** | Vector difference using vecdiff expression |
| **at** | Chain V2 to V1's tip using chain expression |
| **Chain (Tip-to-Tail)** | Project V1 onto V2 using vecproject expression |
| **Project A onto B** | Angle between two vectors |
| **Angle Between** | Dot product of two vectors |
| **Dot Product** | Cross product of two vectors (2D returns scalar) |
| **Cross Product** |  |

## Expression Details

**Vector sum using vecsum expression**

```
vecsum(G, V1, V2) or vecsum(G, V1, V2, point)
```

**Vector difference using vecdiff expression**

```
vecdiff(G, V1, V2) or vecdiff(G, V1, V2, point)
```

**Chain V2 to V1's tip using chain expression**

```
chain(G, V1, V2)
```

**Project V1 onto V2 using vecproject expression**

```
vecproject(G, V1, V2)
```

**Angle between two vectors**

```
angle(G, V1, V2, type(interior), radius(0.2))
```

**Dot product of two vectors**

```
property(V1, 'dot', V2)
```

**Cross product of two vectors (2D returns scalar)**

```
property(V1, 'cross', V2)
```
