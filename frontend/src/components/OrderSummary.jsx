import React from 'react';

export default function OrderSummary({ structured }) {
  if (!structured) return null;
  const { items, suggestions = [] } = structured;
  const total = items.reduce((s, i) => s + i.price * i.quantity, 0);
  return (
    <aside className="order-summary">
      <h2>Your Order</h2>
      <ul>
        {items.map((i, idx) => (
          <li key={idx}>{i.quantity}× {i.size} {i.name} - ${i.price * i.quantity}</li>
        ))}
        <li className="order-total">Total: ${total}</li>
      </ul>
      {suggestions.length > 0 && (
        <div className="order-suggestions">
          Suggestions: {suggestions.map(s => s.text).join(', ')}
        </div>
      )}
      <button className="checkout-btn">Checkout</button>
    </aside>
  );
}