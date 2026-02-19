import { useState, useEffect } from 'react';
import TaskForm from './components/TaskForm';
import TaskList from './components/TaskList';
import TaskStats from './components/TaskStats';
import FilterBar from './components/FilterBar';

const API_URL = 'http://localhost:8000';

function App() {
  const [tasks, setTasks] = useState([]);
  const [stats, setStats] = useState({ total: 0, todo: 0, doing: 0, done: 0 });
  const [filter, setFilter] = useState({ status: null, priority: null });
  const [editingTask, setEditingTask] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Fetch tasks från API
  const fetchTasks = async () => {
    setLoading(true);
    setError(null);
    try {
      const params = new URLSearchParams();
      if (filter.status) params.append('status', filter.status);    
      if (filter.priority) params.append('priority', filter.priority);
      
      const response = await fetch(`${API_URL}/tasks/?${params}`);
      if (!response.ok) throw new Error('Failed to fetch tasks');
      const data = await response.json();
      setTasks(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  // Fetch statistik
  const fetchStats = async () => {
    try {
      const response = await fetch(`${API_URL}/tasks/stats/summary`);
      if (!response.ok) throw new Error('Failed to fetch stats');
      const data = await response.json();
      setStats(data);
    } catch (err) {
      console.error('Stats error:', err);
    }
  };

  useEffect(() => {     
    fetchTasks();
    fetchStats();
  }, [filter]);

  // CREATE - Skapa ny task
  const createTask = async (taskData) => {
    try {
      const response = await fetch(`${API_URL}/tasks/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(taskData),
      });
      if (!response.ok) throw new Error('Failed to create task');
      await fetchTasks();
      await fetchStats();
    } catch (err) {
      setError(err.message);
    }
  };

  // UPDATE - Uppdatera task
  const updateTask = async (taskId, taskData) => {
    try {
      const response = await fetch(`${API_URL}/tasks/${taskId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(taskData),
      });
      if (!response.ok) throw new Error('Failed to update task');
      await fetchTasks();
      await fetchStats();
      setEditingTask(null);
    } catch (err) {
      setError(err.message);
    }
  };

  // DELETE - Ta bort task
  const deleteTask = async (taskId) => {
    if (!window.confirm('Är du säker på att du vill ta bort denna task?')) return;
    
    try {
      const response = await fetch(`${API_URL}/tasks/${taskId}`, {
        method: 'DELETE',
      });
      if (!response.ok) throw new Error('Failed to delete task');
      await fetchTasks();
      await fetchStats();
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="container mx-auto px-4 py-8 max-w-6xl">
        {/* Header */}
        <header className="mb-8">
          <h1 className="text-4xl font-bold text-gray-800 mb-2">
            📋 Task Tracker
          </h1>
          <p className="text-gray-600">
            Håll koll på dina uppgifter och öka produktiviteten
          </p>
        </header>

        {/* Error message */}
        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
            {error}
          </div>
        )}

        {/* Stats */}
        <TaskStats stats={stats} />

        {/* Filter Bar */}
        <FilterBar filter={filter} setFilter={setFilter} />

        {/* Main Content Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Task Form */}
          <div className="lg:col-span-1">
            <TaskForm
              onSubmit={editingTask ? (data) => updateTask(editingTask.id, data) : createTask}
              editingTask={editingTask}
              onCancelEdit={() => setEditingTask(null)}
            />
          </div>

          {/* Task List */}
          <div className="lg:col-span-2">
            <TaskList
              tasks={tasks}
              loading={loading}
              onEdit={setEditingTask}
              onDelete={deleteTask}
              onStatusChange={(taskId, status) => updateTask(taskId, { status })}
            />
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;