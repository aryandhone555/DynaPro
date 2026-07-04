import api from "../api/axios";
import { ENDPOINTS } from "../api/endpoints";

export const getTopOffenders = async () => {
  const response = await api.get(ENDPOINTS.TOP_OFFENDERS);
  return response.data;
};