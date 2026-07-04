import { useEffect, useState } from "react";
import { getTopOffenders } from "../../services/topOffendersService";
import HealthBadge from "./HealthBadge";

function TopOffenders() {
  const [offenders, setOffenders] = useState([]);

  useEffect(() => {
    const fetchOffenders = async () => {
      try {
        const data = await getTopOffenders();
        setOffenders(data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchOffenders();
  }, []);

  return (
    <div className="bg-slate-800 rounded-xl p-6 h-full">

      <h2 className="text-xl font-bold text-white mb-5">
        🏆 Top Offenders
      </h2>

      <div className="space-y-4">

        {offenders.length === 0 ? (
          <p className="text-gray-400">
            No offenders found
          </p>
        ) : (
          offenders.map((resource, index) => (
            <div
              key={resource.resource_id}
              className="border border-slate-700 rounded-lg p-4"
            >
              <div className="flex justify-between items-center">

                <div>

                  <h3 className="text-white font-semibold">
                    #{index + 1} {resource.resource_name}
                  </h3>

                  <p className="text-gray-400 text-sm mt-1">
                    {resource.resource_type}
                  </p>

                </div>

                <HealthBadge status={resource.status} />

              </div>
            </div>
          ))
        )}

      </div>

    </div>
  );
}

export default TopOffenders;