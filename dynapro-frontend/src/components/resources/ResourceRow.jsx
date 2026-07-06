function ResourceRow({ resource }) {
  return (
    <tr className="border-b border-slate-700 hover:bg-slate-700/50 transition-colors duration-200">

      <td className="px-6 py-4 font-medium text-white">
        {resource.name}
      </td>

      <td className="px-6 py-4 text-slate-300">
        {resource.resource_type}
      </td>

      <td className="px-6 py-4 text-slate-300">
        {resource.environment}
      </td>

      <td className="px-6 py-4">
        <span
          className={`px-3 py-1 rounded-full text-xs font-semibold
            ${
              resource.status === "GREEN"
                ? "bg-green-600 text-white"
                : resource.status === "AMBER"
                ? "bg-yellow-500 text-black"
                : "bg-red-600 text-white"
            }`}
        >
          {resource.status}
        </span>
      </td>

      <td className="px-6 py-4 text-slate-300">
        {resource.metrics_count.toLocaleString()}
      </td>

      <td className="px-6 py-4 text-slate-400">
        {new Date(resource.last_updated).toLocaleString()}
      </td>

    </tr>
  );
}

export default ResourceRow;