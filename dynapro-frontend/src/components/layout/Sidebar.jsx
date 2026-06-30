function Sidebar() {
  return (
    <aside className="w-64 bg-slate-800 text-white p-6">
      <h1 className="text-2xl font-bold mb-10">
        DynaPro
      </h1>

      <nav className="space-y-4">
        <button className="block w-full text-left hover:text-cyan-400">
          Dashboard
        </button>

        <button className="block w-full text-left hover:text-cyan-400">
          Resources
        </button>

        <button className="block w-full text-left hover:text-cyan-400">
          Alerts
        </button>
      </nav>
    </aside>
  );
}

export default Sidebar;