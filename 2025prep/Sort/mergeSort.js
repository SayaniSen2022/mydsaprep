let arr = [1, 8, 9, 1, 3, 5, 6, 6, 5]; // Removed the extra comma

function mergeSort(arr, low, high) {
  if (low >= high) return; // Changed condition to handle base case better

  let mid = Math.floor((low + high) / 2); // Fixed mid calculation

  mergeSort(arr, low, mid);
  mergeSort(arr, mid + 1, high);
  merge(arr, low, mid, high);
}

function merge(arr, low, mid, high) {
  let temp = [];
  let left = low;
  let right = mid + 1;

  while (left <= mid && right <= high) {
    if (arr[left] < arr[right]) {
      temp.push(arr[left]);
      left++;
    } else {
      temp.push(arr[right]);
      right++;
    }
  }

  while (left <= mid) {
    temp.push(arr[left]);
    left++;
  }
  while (right <= high) {
    temp.push(arr[right]);
    right++;
  }

  for (let i = low; i <= high; i++) {
    arr[i] = temp[i - low];
  }
}

// To use the function:
mergeSort(arr, 0, arr.length - 1); // Changed indices to cover whole array
console.log(arr); // Print the array directly
