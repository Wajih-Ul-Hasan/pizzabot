import React from 'react'
import MessageList from './MessageList'
import OrderSummary from './OrderSummary'

export default function ChatWindow({ messages, structured }) {
  return (
    <div className="chat-container container py-3">
      <h4 className="text-center">PizzaBot</h4>
      <MessageList items={messages} />
      <OrderSummary structured={structured} />
    </div>
  )
}