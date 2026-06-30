import { useEffect, useState } from "react";

import Sidebar from "../../components/layout/Sidebar";
import Navbar from "../../components/layout/Navbar";
import SummaryCard from "../../components/dashboard/SummaryCard";

import { getDashboardSummary } from "../../services/dashboardService";

function Dashboard() {
  const [summary, setSummary] = useState(null);

  useEffect(() => {
    const fetchSummary = async () => {
      try {
        const data = await getDashboardSummary();
        setSummary(data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchSummary();
  }, []);

  if (!summary) {
    return (
      <div className="text-white flex justify-center items-center h-screen bg-slate-900">
        Loading...
      </div>
    );
  }

  return (
    <div className="flex h-screen bg-slate-900">

      <Sidebar />

      <div className="flex-1 flex flex-col">

        <Navbar />

        <main className="p-6">

          <div className="grid grid-cols-4 gap-6">

            <SummaryCard
              title="Total Resources"
              value={summary.total_resources}
              color="bg-slate-800 text-white"
            />

            <SummaryCard
              title="Green"
              value={summary.green}
              color="bg-green-700 text-white"
            />

            <SummaryCard
              title="Amber"
              value={summary.amber}
              color="bg-yellow-600 text-white"
            />

            <SummaryCard
              title="Red"
              value={summary.red}
              color="bg-red-700 text-white"
            />

          </div>

        </main>

      </div>

    </div>
  );
}

export default Dashboard;