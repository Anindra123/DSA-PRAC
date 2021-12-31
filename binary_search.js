//binary search algorithm
//recursive search algorithm
const prompt = require("prompt-sync")({ sigint: true });
function bubble_sort(arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length; j++) {
      if (arr[j + 1] < arr[j]) {
        [arr[j + 1], arr[j]] = [arr[j], arr[j + 1]];
      }
    }
  }
  return arr;
}
function binary_search_algo(arr, left, right, elem) {
  let result;
  let mid = Math.floor((right + left) / 2);
  if (arr[mid] === elem) {
    return mid;
  } else if (left > right) {
    return -1;
  } else if (arr[mid] > elem) {
    //look for the left side of array
    result = binary_search_algo(arr, left, mid - 1, elem);
  } else if (arr[mid] < elem) {
    //look for right side of array
    result = binary_search_algo(arr, mid + 1, right, elem);
  }
  return result;
}

//first the list needs to be sorted
function binary_search(arr, elem) {
  let result = binary_search_algo(arr, 0, arr.length - 1, elem);
  if (result < 0) {
    return `Not found`;
  }
  return `Element found at index ${result} and elem : ${arr[result]}`;
}

function main() {
  let arr = [10, 5, 1, 2, 9, 6, 7, 0, 4, 12];
  let s_arr = bubble_sort(arr);
  const num = prompt("Enter an number :");
  console.log(s_arr);
  console.log(binary_search(s_arr, Number(num)));
}
main();
