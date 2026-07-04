function Sidebar({ conversations, activeConversationId, onSelect, onNew, onDelete }) {
  return (
    <aside className="sidebar">
      <button type="button" className="sidebar-new-btn" onClick={onNew}>
        <svg
          viewBox="0 0 24 24"
          width="16"
          height="16"
          fill="none"
          stroke="currentColor"
          strokeWidth="2.2"
          strokeLinecap="round"
          strokeLinejoin="round"
          aria-hidden="true"
        >
          <line x1="12" y1="5" x2="12" y2="19" />
          <line x1="5" y1="12" x2="19" y2="12" />
        </svg>
        New conversation
      </button>

      <nav className="sidebar-list" aria-label="Conversations">
        {conversations.map((conversation) => {
          const isActive = conversation.id === activeConversationId
          return (
            <div
              key={conversation.id}
              className={`sidebar-item${isActive ? ' sidebar-item-active' : ''}`}
            >
              <button
                type="button"
                className="sidebar-item-button"
                onClick={() => onSelect(conversation.id)}
                aria-current={isActive ? 'true' : undefined}
              >
                {conversation.title}
              </button>
              <button
                type="button"
                className="sidebar-item-delete"
                aria-label={`Delete conversation "${conversation.title}"`}
                onClick={() => onDelete(conversation.id)}
              >
                ×
              </button>
            </div>
          )
        })}
      </nav>
    </aside>
  )
}

export default Sidebar
