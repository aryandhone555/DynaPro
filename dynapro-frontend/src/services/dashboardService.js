import api from "../api/axios";

export const getDashboardSummary = async () => {
  const token = localStorage.getItem("access");

  const response = await api.get("/dashboard/summary/", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return response.data;
};