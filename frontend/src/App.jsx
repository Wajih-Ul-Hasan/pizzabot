import React, { useState } from 'react'
import ChatWindow from './components/ChatWindow'
import ChatInput from './components/ChatInput'
import { sendMessage } from './api'
import './index.css'

export default function App() {
  const [messages, setMessages] = useState([])
  const [structured, setStructured] = useState(null)
  const [loading, setLoading] = useState(false)
  const sessionId = 'demo-session'

  async function handleSend(text) {
    setLoading(true)
    const next = [...messages, { role: 'user', content: text }]
    setMessages(next)
    try {
      const res = await sendMessage(sessionId, text)
      setMessages(m => [...m, { role: 'bot', content: res.reply }])
      setStructured(res.structured)
    } catch (e) {
      setMessages(m => [...m, { role: 'bot', content: 'Error contacting server' }])
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="d-flex flex-column" style={{minHeight: '100vh'}}>
      <ChatWindow messages={messages} structured={structured} />
      <ChatInput onSend={handleSend} loading={loading} />
    </div>
  )
}