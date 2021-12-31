//bubble sort alogrithm

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

function main() {
  let un_sorted = [5, 4, 1, 2, 11, 12, 0, 2, 3, 10, 9];
  let sorted = bubble_sort(un_sorted);
  console.log(sorted);
}

main();
