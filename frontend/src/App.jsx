import React, { useState } from 'react';
import ChatWindow from './components/ChatWindow';
import ChatInput from './components/ChatInput';
import './App.css';

export default function App() {
  const [messages, setMessages] = useState([]);
  const [structured, setStructured] = useState(null);
  const [loading, setLoading] = useState(false);

  // Dummy send handler for preview
  function handleSend(text) {
    setLoading(true);
    setMessages([...messages, { role: 'user', content: text }]);
    setTimeout(() => {
      setMessages(m => [...m, { role: 'bot', content: 'PizzaBot reply!' }]);
      setStructured({
        intent: 'order',
        items: [{ name: 'Pepperoni', size: 'Large', quantity: 1, price: 12 }],
        notes: '',
        suggestions: [{ text: 'Try garlic bread!' }]
      });
      setLoading(false);
    }, 1000);
  }

  return (
    <div className="pizza-app">
      <header className="pizza-header">
        <img src="/vite.svg" alt="PIZZABOT Logo" className="logo" />
        <h1>PIZZABOT</h1>
        <p className="subtitle">Order pizza with AI-powered chat!</p>
      </header>
      <main className="pizza-main">
        <ChatWindow messages={messages} structured={structured} />
        <ChatInput onSend={handleSend} loading={loading} />
      </main>
      <footer className="pizza-footer">
        <p>© 2025 PIZZABOT. All rights reserved.</p>
      </footer>
    </div>
  );
}