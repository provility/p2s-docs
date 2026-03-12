---
title: "Vector 3D + Vector 3D"
sidebar_label: "Vector 3D + Vector 3D"
---

# Vector 3D + Vector 3D

Operations available when you select a **vector3d** and a **vector3d** together.

## How to Use

```
  1. Click on a vector3d object to select it
  2. Hold Shift and click on a vector3d object
  3. Right-click to open the context menu
  4. Choose an operation from the menu
```

## Available Operations

| Operation | Description |
|-----------|-------------|
| **Sum (A + B)** | Handler for two 3D vector selection |
| **at** | Vector sum using vecsum3d expression |
| **Difference (A - B)** | Vector difference using vecdiff3d expression |
| **at** | Chain V2 to V1's tip using chain3d expression |
| **Chain (Tip-to-Tail)** | Project V1 onto V2 using vecproject3d expression |
| **Project A onto B** | Create angle between two vectors |
| **Angle** | Create a 3D plane from two spanning vectors and a point |
| **Plane** |  |

## Expression Details

**Vector sum using vecsum3d expression**

```
vecsum3d(V1, V2) or vecsum3d(V1, V2, point)
```

**Vector difference using vecdiff3d expression**

```
vecdiff3d(V1, V2) or vecdiff3d(V1, V2, point)
```

**Chain V2 to V1's tip using chain3d expression**

```
chain3d(V1, V2)
```

**Project V1 onto V2 using vecproject3d expression**

```
vecproject3d(V1, V2)
```

**Create angle between two vectors**

```
angle3d(G, V1, V2)
```

**Create a 3D plane from two spanning vectors and a point**

```
plane3d(G, V1, V2, point3d(G, px, py, pz))
```
