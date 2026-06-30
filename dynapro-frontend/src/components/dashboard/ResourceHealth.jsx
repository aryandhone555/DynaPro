import { useEffect, useState } from "react";
import { getResourceHealth } from "../../services/resourceService";
import HealthBadge from "./HealthBadge";

function ResourceHealth() {
  const [resources, setResources] = useState([]);

  useEffect(() => {
    const fetchResources = async () => {
      try {
        const data = await getResourceHealth();
        setResources(data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchResources();
  }, []);

  return (
    <div className="bg-slate-800 rounded-xl p-6 mt-8">

      <h2 className="text-xl font-bold text-white mb-4">
        Resource Health
      </h2>

      <table className="w-full text-white">

        <thead>
          <tr className="border-b border-slate-700">
            <th className="text-left py-3">Resource</th>
            <th className="text-left">Type</th>
            <th className="text-left">Status</th>
            <th className="text-left">Last Updated</th>
          </tr>
        </thead>

        <tbody>

          {resources.map((resource) => (

            <tr
              key={resource.resource_id}
              className="border-b border-slate-700"
            >

              <td className="py-4">
                {resource.resource_name}
              </td>

              <td>
                {resource.resource_type}
              </td>

              <td>
                <HealthBadge
                  status={resource.status}
                />
              </td>

              <td>
                {new Date(
                  resource.last_updated
                ).toLocaleString()}
              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}

export default ResourceHealth;