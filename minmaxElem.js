let recurNum = 0;
function dac_max(arr, index, l) {
  recurNum++;
  //check left side
  let max;
  if (index >= l - 2) {
    if (arr[index] > arr[index + 1]) {
      return arr[index];
    } else {
      return arr[index + 1];
    }
  }
  //right side
  max = dac_max(arr, index + 1, l);

  if (arr[index] > max) {
    return arr[index];
  } else {
    return max;
  }
}

function dac_min(arr, index, len) {
  let min;
  if (index >= len - 2) {
    if (arr[index] < arr[index + 1]) {
      return arr[index];
    } else {
      return arr[index + 1];
    }
  }
  min = dac_min(arr, index + 1, len);
  if (arr[index] < min) {
    return arr[index];
  } else {
    return min;
  }
}

function main() {
  let arr = [4, 10, 1, 5, 6];
  let max = dac_max(arr, 0, arr.length);
  let min = dac_min(arr, 0, arr.length);
  console.log(`Max value : ${max}`);
  console.log(`Min value : ${min}`);
  console.log(`Number of recursion : ${recurNum}`);
}

main();
