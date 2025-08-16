import React from 'react'

export default function MessageList({ items }) {
  return (
    <div className="messages">
      {items.map((m, i) => (
        <div key={i} className={`message ${m.role}`}>{m.content}</div>
      ))}
    </div>
  )
}