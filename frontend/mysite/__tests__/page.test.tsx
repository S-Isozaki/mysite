import Link from 'next/link'
import '@testing-library/jest-dom/jest-globals'
import { render, screen } from '@testing-library/react'
import { describe, it, expect } from '@jest/globals'

export default function Home() {
  return (
    <div>
      <h1>Home</h1>
      <Link href="/about">About</Link>
    </div>
  )
}

describe('Page', () => {
  it('renders a heading', () => {
    render(<Home />)
 
    const heading = screen.getByRole('heading', { level: 1 })
 
    expect(heading).toBeInTheDocument()
  })
})