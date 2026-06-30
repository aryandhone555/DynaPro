function HealthBadge({ status }) {
  const colors = {
    GREEN: "bg-green-600",
    AMBER: "bg-yellow-500 text-black",
    RED: "bg-red-600",
  };

  return (
    <span
      className={`px-3 py-1 rounded-full text-sm font-semibold ${
        colors[status] || "bg-gray-500"
      }`}
    >
      {status}
    </span>
  );
}

export default HealthBadge;