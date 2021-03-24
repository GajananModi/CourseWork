--- q1 ----



-we create array of numbers 1 to n where n is the i/p given through i/p file
-then we divide that array equally according to number of process
-resiprocal some is calculated parallely and then we merge it at main process






----q2(parallel quick sort)-----------------
- we divide the array according to number of process
- each part of array implement their quicksort individually
- then we merge all sorted array receive by process (2 array at time)
  (actually we run the for loop logp times to merge all p arrays where p is number of process 
