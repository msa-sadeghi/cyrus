const trade = {
  symbol: "nvidia",
  type: "buy",
  quantity: 100,
  price: 25000,
  date: "2026-05-31",
};
let trades = [];
const form = document.getElementById("tradeForm");
const btn = document.querySelector("button");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const trade = {
    symbol: symbol.value,
    type: type.value,
    quantity: quantity.value,
    price: price.value,
    date: new Date(),
  };
  trades.push(trade);
  localStorage.setItem("trades", JSON.stringify(trades));
  renderHistory();
});

function renderHistory() {
  historyElement.innerHTML = "";
  trades.forEach((t) => {
    historyElement.innerHTML += `
    <p>
    ${t.type}
    ${t.symbol}
    ${t.quantity}
    <p/>`;
  });
}

window.onload = function () {
  trades = JSON.parse(localStorage.getItem("trades")) || [];
  renderHistory();
};
