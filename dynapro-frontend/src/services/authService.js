import api from "../api/axios";

export const login = async (username, password) => {
  const response = await api.post("/token/", {
    username,
    password,
  });

  return response.data;
};

export const getCurrentUser = async () => {
  const token = localStorage.getItem("access");

  const response = await api.get("/me/", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return response.data;
};