// THIS PAGE FOR INSTRUCTIONS: https://wagmi.sh/examples/send-transaction#step-1-connect-wallet

import React from 'react'

export function SendTransaction() {
  const [to, setTo] = React.useState('')

  const [amount, setAmount] = React.useState('')

  return (
    <form>
      <input
        aria-label="Recipient"
        onChange={(e) => setTo(e.target.value)}
        placeholder="0xA0Cf…251e"
        value={to}
      />
      <input
        aria-label="Amount (ether)"
        onChange={(e) => setAmount(e.target.value)}
        placeholder="0.05"
        value={amount}
      />
      <button disabled={!to || !amount}>Send</button>
    </form>
  )
}
