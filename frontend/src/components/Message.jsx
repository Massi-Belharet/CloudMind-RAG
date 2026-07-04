import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'

function Message({ role, content, isLoading = false }) {
  const isAssistant = role === 'assistant'

  return (
    <div className={`message-row message-row-${role}`}>
      <div className="message-row-inner">
        <div className="message-role">{isAssistant ? 'CloudMind' : 'You'}</div>
        <div className="message-content">
          {isLoading ? (
            <span className="typing-indicator" role="status">
              <span className="typing-dot" />
              <span className="typing-dot" />
              <span className="typing-dot" />
              <span className="sr-only">CloudMind is thinking</span>
            </span>
          ) : isAssistant ? (
            <ReactMarkdown remarkPlugins={[remarkGfm]}>{content}</ReactMarkdown>
          ) : (
            content
          )}
        </div>
      </div>
    </div>
  )
}

export default Message
