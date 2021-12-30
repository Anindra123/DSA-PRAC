//selection sor

function selection_sort(arr) {
  //set the current element in the array as smallest
  for (let i = 0; i < arr.length; i++) {
    let curr_small = arr[i];
    let small_idx = i;
    //look for the array if any element is smaller than current
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[j] < curr_small) {
        curr_small = arr[j];
        small_idx = j;
      }
    }
    //replace the current element with the smallest element in array
    [arr[i], arr[small_idx]] = [arr[small_idx], arr[i]];
  }
  return arr;
}

function main() {
  let un_sorted = [5, 4, 1, 2, 2, 3, 10, 0, 11];
  let sorted = selection_sort(un_sorted);
  console.log(sorted);
}

main();
