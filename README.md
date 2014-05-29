VoxelPathTracer
===============

Trace 2d-3d paths using a voxel estimation.

Includes built in virtualization of the result.

View Commands:
  arrow keys, z, Z + w, a, s, d, q, e - Rotates the view.
  r - Resets view rotation.
  
Output:
  Breaks down paths into a series of left, right, forward, back commands.
  Useful for AI pathfinding in voxelized space.
  Can also be used for general curve approximation.
  
Theory:
  Instead of a classic Monte-Carlo or Ceill approximation I instead walk the curve.
  My program introduces a cursor that follows the curve, creating voxels as it moves.
  
  The cursor can only move in a direction perpendicular to one of its faces. This ensure
  the trace is confined to a voxel grid.
  
  By recording the cursor's motion a rough voxel trace is generated.
