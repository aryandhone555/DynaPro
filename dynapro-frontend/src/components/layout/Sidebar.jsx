import { NavLink } from "react-router-dom";
function Sidebar() {
  return (
    <aside className="w-64 bg-slate-800 text-white p-6">
      <h1 className="text-2xl font-bold mb-10">
        DynaPro
      </h1>

      <NavLink
        to="/dashboard"
        className={({ isActive }) =>
         `block rounded-lg px-3 py-2 transition ${
         isActive
        ? "bg-cyan-600 text-white"
        : "hover:bg-slate-700 hover:text-cyan-400"
        }`
        }
        >
         Dashboard
      </NavLink>

      <NavLink
  to="/resources"
  className={({ isActive }) =>
    `block rounded-lg px-3 py-2 transition ${
      isActive
        ? "bg-cyan-600 text-white"
        : "hover:bg-slate-700 hover:text-cyan-400"
    }`
  }
>
  Resources
</NavLink>

<NavLink
  to="/alerts"
  className={({ isActive }) =>
    `block rounded-lg px-3 py-2 transition ${
      isActive
        ? "bg-cyan-600 text-white"
        : "hover:bg-slate-700 hover:text-cyan-400"
    }`
  }
>
  Alerts
</NavLink>
      
    </aside>
  );
}

export default Sidebar;