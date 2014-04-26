VoxelPathTracer
===============

Trace 2d-3d paths using a voxel estimation.

Includes built in virtualization of the result.

View Commands
  arrow keys, z, Z + w, a, s, d, q, e - Rotates the view.
  r - Resets view rotation.
  
Output
  Breaks down paths into a series of left, right, forward, back commands.
  Useful for AI pathfinding in voxelized space.
  Can also be used for general curve approximation.
  
Theory
  Instead of a classic Monte-Carlo approximation I instead walk the curve.
  My program introduces a cursor that attempts to trace the curve, and places
  voxels beneath it as it moves.
  
  Since the cursor is square the code checks how close the curve is to each of its
  edges and moves in the direction that is closest.
  
  By recording the cursor's location as it follows the curve it is possible to
  generate a rough voxel trace.
