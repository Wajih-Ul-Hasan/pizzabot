import React from 'react';

export default function MessageList({ items }) {
  return (
    <ul className="message-list">
      {items.map((m, i) => (
        <li key={i} className={`message ${m.role}`}>
          <div className="message-card">{m.content}</div>
        </li>
      ))}
    </ul>
  );
}