import api from "../api/axios";
import { ENDPOINTS } from "../api/endpoints";

export const getAlerts = async () => {
  const response = await api.get(ENDPOINTS.ALERTS);
  return response.data;
};