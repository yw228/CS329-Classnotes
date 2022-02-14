/** 
sorts the array from least to greatest

@requires array != null

@ensures for all i in indices(out), i < out.size()-1 ==> out[i] < out[i+1]

@ensures forall i, i in out <==> i in array
// `out` must have all elements in `array` and only elements from `arrary`


@ensures out.size() == array.size()

@param array array to be sorted
@return (out: Vector<Integer>) a sorted version of array
*/






Equivalence partitioning with bounary value analysis
1. Separate input to partition(valid and invalid)
2. Determine the boundaries
3. Test each partition

example static Vector<int> sort (Vector<Integer> array) {}

// invalid partition 
null | 0 | 4 -> max input
boolean (java) T/F


single test for each partition
tests on the boundaries 







