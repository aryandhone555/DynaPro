import { useEffect, useState } from "react";
import { getAlerts } from "../../services/alertService";
import HealthBadge from "./HealthBadge";

function AlertsPanel() {
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    const fetchAlerts = async () => {
      try {
        const data = await getAlerts();
        setAlerts(data);
      } catch (err) {
        console.error(err);
      }
    };

    fetchAlerts();
  }, []);

  return (
    <div className="bg-slate-800 rounded-xl p-6 h-full">

      <div className="flex justify-between items-center mb-5">

        <h2 className="text-xl font-bold text-white">
          Active Alerts
        </h2>

        <span className="bg-red-600 text-white rounded-full px-3 py-1 text-sm">
          {alerts.length}
        </span>

      </div>

      <div className="space-y-4">

        {alerts.length === 0 ? (
          <p className="text-gray-400">
            No active alerts
          </p>
        ) : (
          alerts.map((alert) => (

            <div
              key={alert.id}
              className="border border-slate-700 rounded-lg p-4"
            >

              <div className="flex justify-between">

                <h3 className="text-white font-semibold">
                  {alert.resource_name}
                </h3>

                <HealthBadge status={alert.status} />

              </div>

              <p className="text-gray-400 mt-2">
                {alert.message}
              </p>

            </div>

          ))
        )}

      </div>

    </div>
  );
}

export default AlertsPanel;