import React from 'react'

export default function OrderSummary({ structured }) {
  if (!structured) return null
  const { intent, items, notes, suggestions = [] } = structured
  const total = items.reduce((s, i) => s + i.price * i.quantity, 0)
  return (
    <div className="p-3 border-top">
      <h6 className="mb-2">Order</h6>
      {items.length === 0 ? <div className='text-muted'>No items yet</div> : (
        <ul className="list-group mb-2">
          {items.map((i, idx) => (
            <li key={idx} className="list-group-item d-flex justify-content-between">
              <span>{i.quantity}× {i.size} {i.name}</span>
              <span>${(i.price * i.quantity).toFixed(2)}</span>
            </li>
          ))}
          <li className="list-group-item d-flex justify-content-between fw-bold">
            <span>Total</span><span>${total.toFixed(2)}</span>
          </li>
        </ul>
      )}
      {suggestions.length > 0 && (
        <div className="small text-muted">Suggestions: {suggestions.map(s=>s.text).join(', ')}</div>
      )}
    </div>
  )
}