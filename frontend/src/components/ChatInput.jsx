import React, { useState } from 'react'

export default function ChatInput({ onSend, loading }) {
  const [text, setText] = useState('')
  const submit = (e) => {
    e.preventDefault()
    if (!text.trim()) return
    onSend(text.trim())
    setText('')
  }
  return (
    <form onSubmit={submit} className="d-flex gap-2 p-3 border-top">
      <input className="form-control" placeholder="Type a message" value={text} onChange={e=>setText(e.target.value)} disabled={loading} />
      <button className="btn btn-primary" disabled={loading}>Send</button>
    </form>
  )
}