import React, { useState } from 'react';

export default function ChatInput({ onSend, loading }) {
  const [text, setText] = useState('');
  const submit = e => {
    e.preventDefault();
    if (!text.trim()) return;
    onSend(text.trim());
    setText('');
  };
  return (
    <form onSubmit={submit} className="chat-input">
      <input
        className="chat-input-field"
        placeholder="Type a message"
        value={text}
        onChange={e => setText(e.target.value)}
        disabled={loading}
      />
      <button className="chat-send-btn" disabled={loading}>Send</button>
    </form>
  );
}