const FilterBar = ({ filter, setFilter }) => {
  const handleFilterChange = (type, value) => {
    setFilter(prev => ({
      ...prev,
      [type]: value === 'all' ? null : value,
    }));
  };

  return (
    <div className="bg-white rounded-lg shadow-md p-4 mb-6">
      <div className="flex flex-wrap gap-4 items-center">
        <div className="flex items-center gap-2">
          <span className="text-sm font-medium text-gray-700">Filtrera:</span>
        </div>

        <div className="flex items-center gap-2">
          <label className="text-sm text-gray-600">Status:</label>
          <select
            value={filter.status || 'all'}
            onChange={(e) => handleFilterChange('status', e.target.value)}
            className="px-3 py-1 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="all">Alla</option>
            <option value="todo">📝 To Do</option>
            <option value="doing">⚙️ In Progress</option>
            <option value="done">✅ Done</option>
          </select>
        </div>

        <div className="flex items-center gap-2">
          <label className="text-sm text-gray-600">Prioritet:</label>
          <select
            value={filter.priority || 'all'}
            onChange={(e) => handleFilterChange('priority', e.target.value)}
            className="px-3 py-1 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="all">Alla</option>
            <option value="low">🟢 Låg</option>
            <option value="medium">🟡 Medium</option>
            <option value="high">🔴 Hög</option>
          </select>
        </div>

        {(filter.status || filter.priority) && (
          <button
            onClick={() => setFilter({ status: null, priority: null })}
            className="px-3 py-1 bg-gray-200 text-gray-700 text-sm rounded-md hover:bg-gray-300 transition-colors"
          >
            🔄 Rensa filter
          </button>
        )}
      </div>
    </div>
  );
};

export default FilterBar;
