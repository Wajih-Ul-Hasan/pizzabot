export async function sendMessage(sessionId, message, history = []) {
  const res = await fetch('/api/chat/send', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ session_id: sessionId, message, history })
  })
  if (!res.ok) throw new Error('Network error')
  return res.json()
}

export async function fetchMenu() {
  const res = await fetch('/api/order/menu')
  return res.json()
}