// Best time to Buy and Sell Stock: You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

let prices = [7, 1, 5, 3, 6, 4];

var maxProfit = function (prices) {
  let [left, right, max] = [0, 1, 0];

  while (right < prices.length) {
    if (prices[right] <= prices[left]) left = right;

    let profit = prices[right] - prices[left];
    max = Math.max(max, profit);

    right++;
  }
  return max;
};

console.log(maxProfit(prices));
