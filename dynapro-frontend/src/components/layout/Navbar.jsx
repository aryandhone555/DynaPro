import { useNavigate } from "react-router-dom";

function Navbar() {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");

    navigate("/", { replace: true });
  };

  return (
    <header className="bg-slate-800 h-16 flex items-center justify-between px-6 border-b border-slate-700">
      <h2 className="text-white text-xl font-semibold">
        Dashboard
      </h2>

      <button
        onClick={handleLogout}
        className="bg-red-600 hover:bg-red-700 px-4 py-2 rounded text-white"
      >
        Logout
      </button>
    </header>
  );
}

export default Navbar;