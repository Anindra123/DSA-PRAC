//merge sort
//divide and conquer algorithm

function merge(left, right) {
  const c = [];
  while (left.length && right.length) {
    if (left[0] < right[0]) {
      c.push(left.shift());
    } else {
      c.push(right.shift());
    }
  }
  if (left.length) {
    while (left.length) {
      c.push(left.shift());
    }
  }
  if (right.length) {
    while (right.length) {
      c.push(right.shift());
    }
  }
  return c;
}

function merge_sort(arr) {
  if (arr.length === 1) return arr;
  const mid = Math.floor(arr.length / 2);
  const left = arr.slice(0, mid);
  const left_s = merge_sort(left);
  const right = arr.slice(mid, arr.length);
  const right_s = merge_sort(right);
  return merge(left_s, right_s);
}

function main() {
  let arr = [5, 1, 4, 2, 3];
  let s_array = merge_sort(arr);
  console.log(s_array);
}

main();
