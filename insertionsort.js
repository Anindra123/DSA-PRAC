//insertion sort
function insertion_sort(arr) {
  //set current element indext
  let currIdx = 1;
  while (currIdx < arr.length) {
    for (let i = currIdx; i > 0; i--) {
      //find the correct place for the element
      //to place in the array
      if (arr[i] < arr[i - 1]) {
        [arr[i], arr[i - 1]] = [arr[i - 1], arr[i]];
      } else {
        break;
      }
    }
    currIdx++;
  }
  return arr;
}

function main() {
  let un_sorted = [5, 1, 2, 2, 10, 11, 3, 3, 4, 0];
  let sorted = insertion_sort(un_sorted);
  console.log(un_sorted);
}
main();
