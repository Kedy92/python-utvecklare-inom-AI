const TaskStats = ({ stats }) => {
  const statCards = [
    {
      label: 'Totalt',
      value: stats.total,
      icon: '📊',
      color: 'bg-purple-100 text-purple-800',
    },
    {
      label: 'To Do',
      value: stats.todo,
      icon: '📝',
      color: 'bg-gray-100 text-gray-800',
    },
    {
      label: 'In Progress',
      value: stats.doing,
      icon: '⚙️',
      color: 'bg-blue-100 text-blue-800',
    },
    {
      label: 'Done',
      value: stats.done,
      icon: '✅',
      color: 'bg-green-100 text-green-800',
    },
  ];

  const completionRate = stats.total > 0 
    ? Math.round((stats.done / stats.total) * 100) 
    : 0;

  return (
    <div className="mb-6">
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-4">
        {statCards.map((stat, index) => (
          <div
            key={index}
            className="bg-white rounded-lg shadow-md p-4 text-center"
          >
            <div className="text-3xl mb-2">{stat.icon}</div>
            <div className="text-2xl font-bold text-gray-800">{stat.value}</div>
            <div className="text-sm text-gray-600">{stat.label}</div>
          </div>
        ))}
      </div>

      {/* Progress bar */}
      <div className="bg-white rounded-lg shadow-md p-4">
        <div className="flex justify-between items-center mb-2">
          <span className="text-sm font-medium text-gray-700">Slutförda tasks</span>
          <span className="text-sm font-bold text-gray-800">{completionRate}%</span>
        </div>
        <div className="w-full bg-gray-200 rounded-full h-3">
          <div
            className="bg-gradient-to-r from-green-400 to-green-600 h-3 rounded-full transition-all duration-500"
            style={{ width: `${completionRate}%` }}
          ></div>
        </div>
      </div>
    </div>
  );
};

export default TaskStats;
