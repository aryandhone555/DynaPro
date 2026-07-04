import api from "../api/axios";
import { ENDPOINTS } from "../api/endpoints";

export const getTrends = async () => {
  const response = await api.get(ENDPOINTS.TRENDS);
  return response.data;
};