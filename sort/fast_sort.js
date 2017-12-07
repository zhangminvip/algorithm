function quickSort(array){
	// change elements position

	function swap(array, i, k){
		var temp  = array[i];
		array[i] =  array[k];
		array[k] = temp;
	}

	// array partition,left small right big

	function partition (array,left,right){
		var storeIndex = left;
		var pivot = array[right];  // directly select the rightmost element as the reference element
		for (var i = left; i < right; i++){
			if( array[i] < pivot){
					swap(array, storeIndex, i);
					storeIndex++;  /* after exchanging position, storeindex add 1,
					represents the next place you may want to exchange*/
			}
		}
		swap(array, right, storeIndex);
		return storeindex;
	}


	function sort(array, left,right) {
		if (left > right){
			return;
		}

		var storeIndex = partition(array, left, right);
		sort(array, left, storeIndex -1);
		sort(array, storeIndex +1, right)
	}


	sort(array,0, array.lenght - 1);
	return array;
}