//quick sort algorithm
//divide and conquer algorithm
function hoarePartition(arr, left, right) {
  const mid = Math.floor((left + right) / 2);
  const pivot = arr[mid];
  let l = left - 1;
  let r = right + 1;
  while (true) {
    do {
      l++;
    } while (arr[l] < pivot);
    do {
      r--;
    } while (arr[r] > pivot);
    if (l >= r) return r;
    [arr[l], arr[r]] = [arr[r], arr[l]];
  }
}

function quick_sort_algo(arr, left, right) {
  if (left >= right) return arr;
  const p = hoarePartition(arr, left, right);
  quick_sort_algo(arr, left, p);
  quick_sort_algo(arr, p + 1, right);
  return arr;
}

function main() {
  let arr = [];
  for (let index = 0; index < 500; index++) {
    arr.push(Math.floor(Math.random() * 453));
  }

  let s_arr = quick_sort_algo(arr, 0, arr.length - 1);
  console.log(s_arr);
}
main();
