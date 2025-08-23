import React from 'react';
import MessageList from './MessageList';
import OrderSummary from './OrderSummary';

export default function ChatWindow({ messages, structured }) {
  return (
    <div className="chat-window">
      <MessageList items={messages} />
      <OrderSummary structured={structured} />
    </div>
  );
}