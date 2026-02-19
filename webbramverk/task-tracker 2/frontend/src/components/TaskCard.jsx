const TaskCard = ({ task, onEdit, onDelete, onStatusChange }) => {
  const priorityColors = {
    low: 'bg-green-100 text-green-800',
    medium: 'bg-yellow-100 text-yellow-800',
    high: 'bg-red-100 text-red-800',
  };

  const statusColors = {
    todo: 'bg-gray-100 text-gray-800',
    doing: 'bg-blue-100 text-blue-800',
    done: 'bg-green-100 text-green-800',
  };

  const statusEmojis = {
    todo: '📝',
    doing: '⚙️',
    done: '✅',
  };

  const priorityEmojis = {
    low: '🟢',
    medium: '🟡',
    high: '🔴',
  };

  const formatDate = (dateString) => {
    if (!dateString) return null;
    const date = new Date(dateString);
    return date.toLocaleString('sv-SE', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
    });
  };

  const isOverdue = (deadline) => {
    if (!deadline) return false;
    return new Date(deadline) < new Date() && task.status !== 'done';
  };

  return (
    <div className={`bg-white rounded-lg shadow-md p-4 hover:shadow-lg transition-shadow ${
      isOverdue(task.deadline) ? 'border-l-4 border-red-500' : ''
    }`}>
      <div className="flex items-start justify-between mb-2">
        <div className="flex-1">
          <h3 className="text-lg font-semibold text-gray-800 mb-1">
            {task.title}
          </h3>
          {task.description && (
            <p className="text-gray-600 text-sm mb-2">{task.description}</p>
          )}
        </div>
      </div>

      <div className="flex flex-wrap gap-2 mb-3">
        <span className={`px-2 py-1 rounded-full text-xs font-medium ${statusColors[task.status]}`}>
          {statusEmojis[task.status]} {task.status.toUpperCase()}
        </span>
        <span className={`px-2 py-1 rounded-full text-xs font-medium ${priorityColors[task.priority]}`}>
          {priorityEmojis[task.priority]} {task.priority.toUpperCase()}
        </span>
        {task.deadline && (
          <span className={`px-2 py-1 rounded-full text-xs font-medium ${
            isOverdue(task.deadline) ? 'bg-red-100 text-red-800' : 'bg-purple-100 text-purple-800'
          }`}>
            ⏰ {formatDate(task.deadline)}
          </span>
        )}
      </div>

      <div className="flex items-center gap-2">
        {/* Status snabbval */}
        <select
          value={task.status}
          onChange={(e) => onStatusChange(task.id, e.target.value)}
          className="text-sm px-2 py-1 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          <option value="todo">To Do</option>
          <option value="doing">In Progress</option>
          <option value="done">Done</option>
        </select>

        <div className="flex-1"></div>

        <button
          onClick={() => onEdit(task)}
          className="px-3 py-1 bg-blue-500 text-white text-sm rounded hover:bg-blue-600 transition-colors"
        >
          ✏️ Redigera
        </button>
        <button
          onClick={() => onDelete(task.id)}
          className="px-3 py-1 bg-red-500 text-white text-sm rounded hover:bg-red-600 transition-colors"
        >
          🗑️ Ta bort
        </button>
      </div>

      <div className="mt-2 text-xs text-gray-500">
        Skapad: {formatDate(task.created_at)}
      </div>
    </div>
  );
};

export default TaskCard;
