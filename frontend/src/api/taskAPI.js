import axios from "axios";

const BASE_URL = "http://localhost:8000/api/";

const taskAPI = {};

const tryCatchFetch = async (axiosCall) => {
  try {
    const response = await axiosCall();
    return response.data ? response.data : { message: "success" };
  } catch (e) {
    console.error("-- tryCatchFetch ERROR:", e.response ? e.response.data : e);
    return null;
  }
};

taskAPI.allTasks = async () => {
  return await tryCatchFetch(() => axios.get(`${BASE_URL}tasks/`));
};

export default taskAPI;
