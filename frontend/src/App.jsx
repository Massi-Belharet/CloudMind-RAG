import { useEffect, useState } from 'react'
import Message from './components/Message'
import ChatInput from './components/ChatInput'
import Sidebar from './components/Sidebar'
import { askQuestionStream } from './api'
import { loadConversations, saveConversations } from './storage'
import logo from './assets/logo.png'
import './App.css'

const RESULTS_K = 5
const TITLE_MAX_LENGTH = 40

function createId() {
  return typeof crypto !== 'undefined' && crypto.randomUUID
    ? crypto.randomUUID()
    : `${Date.now()}-${Math.random().toString(36).slice(2)}`
}

function createConversation() {
  return { id: createId(), title: 'New conversation', messages: [] }
}

function deriveTitle(firstMessage) {
  const trimmed = firstMessage.trim()
  if (trimmed.length <= TITLE_MAX_LENGTH) return trimmed
  return `${trimmed.slice(0, TITLE_MAX_LENGTH).trimEnd()}…`
}

function getInitialState() {
  const stored = loadConversations()
  if (stored && Array.isArray(stored.conversations) && stored.conversations.length > 0) {
    return stored
  }
  const initial = createConversation()
  return { conversations: [initial], activeConversationId: initial.id }
}

function App() {
  const [state, setState] = useState(getInitialState)
  const [isLoading, setIsLoading] = useState(false)

  const { conversations, activeConversationId } = state
  const activeConversation = conversations.find((conv) => conv.id === activeConversationId)

  useEffect(() => {
    saveConversations(state)
  }, [state])

  function appendToMessage(conversationId, fragment) {
    setState((prev) => ({
      ...prev,
      conversations: prev.conversations.map((conv) => {
        if (conv.id !== conversationId) return conv
        const messages = [...conv.messages]
        const lastIndex = messages.length - 1
        messages[lastIndex] = { ...messages[lastIndex], content: messages[lastIndex].content + fragment }
        return { ...conv, messages }
      }),
    }))
  }

  function setMessageContent(conversationId, content) {
    setState((prev) => ({
      ...prev,
      conversations: prev.conversations.map((conv) => {
        if (conv.id !== conversationId) return conv
        const messages = [...conv.messages]
        const lastIndex = messages.length - 1
        messages[lastIndex] = { ...messages[lastIndex], content }
        return { ...conv, messages }
      }),
    }))
  }

  async function handleSend(query) {
    const conversationId = activeConversationId

    setState((prev) => ({
      ...prev,
      conversations: prev.conversations.map((conv) => {
        if (conv.id !== conversationId) return conv
        const isFirstMessage = conv.messages.length === 0
        return {
          ...conv,
          title: isFirstMessage ? deriveTitle(query) : conv.title,
          messages: [
            ...conv.messages,
            { role: 'user', content: query },
            { role: 'assistant', content: '' },
          ],
        }
      }),
    }))

    setIsLoading(true)

    try {
      await askQuestionStream(query, RESULTS_K, (fragment) => appendToMessage(conversationId, fragment))
    } catch {
      setMessageContent(
        conversationId,
        "Sorry, I couldn't reach CloudMind. Please check that the backend is running and try again."
      )
    } finally {
      setIsLoading(false)
    }
  }

  function handleNewConversation() {
    const conversation = createConversation()
    setState((prev) => ({
      conversations: [conversation, ...prev.conversations],
      activeConversationId: conversation.id,
    }))
  }

  function handleSelectConversation(conversationId) {
    setState((prev) => ({ ...prev, activeConversationId: conversationId }))
  }

  function handleDeleteConversation(conversationId) {
    setState((prev) => {
      const conversations = prev.conversations.filter((conv) => conv.id !== conversationId)

      if (conversations.length === 0) {
        const fresh = createConversation()
        return { conversations: [fresh], activeConversationId: fresh.id }
      }

      const activeConversationId =
        prev.activeConversationId === conversationId ? conversations[0].id : prev.activeConversationId

      return { conversations, activeConversationId }
    })
  }

  const messages = activeConversation ? activeConversation.messages : []

  return (
    <div className="app-shell">
      <Sidebar
        conversations={conversations}
        activeConversationId={activeConversationId}
        onSelect={handleSelectConversation}
        onNew={handleNewConversation}
        onDelete={handleDeleteConversation}
      />

      <div className="chat-app">
        <header className="chat-header">
          <div className="chat-header-inner">
            <img src={logo} alt="CloudMind logo" className="chat-logo" />
            <div className="chat-header-text">
              <span className="chat-title">CloudMind</span>
              <span className="chat-subtitle">FinOps &amp; Cloud Assistant</span>
            </div>
          </div>
        </header>

        <div className="chat-history">
          {messages.length === 0 && (
            <div className="chat-empty">
              <p>Ask a question about cloud cost optimization, architecture, or compliance to get started.</p>
            </div>
          )}
          {messages.map((message, index) => (
            <Message
              key={index}
              role={message.role}
              content={message.content}
              isLoading={isLoading && index === messages.length - 1 && message.content === ''}
            />
          ))}
        </div>

        <div className="chat-input-area">
          <ChatInput onSend={handleSend} disabled={isLoading} />
        </div>
      </div>
    </div>
  )
}

export default App
