import ResourceRow from "./ResourceRow";

function ResourcesTable({ resources }) {
  return (
    <div className="overflow-hidden rounded-xl border border-slate-700">

      <table className="w-full">

        <thead className="bg-slate-700 text-slate-300 uppercase text-sm">

          <tr>

            <th className="px-6 py-4 text-left">Name</th>

            <th className="px-6 py-4 text-left">Type</th>

            <th className="px-6 py-4 text-left">Environment</th>

            <th className="px-6 py-4 text-left">Status</th>

            <th className="px-6 py-4 text-left">Metrics</th>

            <th className="px-6 py-4 text-left">Last Updated</th>

          </tr>

        </thead>

        <tbody className="bg-slate-800">

          {resources.map((resource) => (
            <ResourceRow
              key={resource.id}
              resource={resource}
            />
          ))}

        </tbody>

      </table>

    </div>
  );
}

export default ResourcesTable;