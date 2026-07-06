import api from "../api/axios";

export const getResourceHealth = async () => {
  const response = await api.get("/dashboard/resource-health/");
  return response.data;
};

export const getResources = async () => {
  const response = await api.get("/resources/");
  return response.data;
};

export const getResource = async (id) => {

    const response = await api.get(
        `/resources/${id}/`
    );

    return response.data;

};