import { useEffect, useState } from "react";
import taskAPI from "../api/taskAPI";
import AllTasks from "../components/AllTasks";

export default function HomePage() {
  const [tasks, setTasks] = useState([]);

  const fetchAllTasks = async () => {
    const data = await taskAPI.allTasks();
    console.log(data);
    setTasks(data ? data : []);
  };

  useEffect(() => {
    fetchAllTasks();
  }, []);

  const renderTasks = () => {
    return tasks.map((task, index) => {
      return <AllTasks task={task} key={index} />;
    });
  };
  return <div>{renderTasks()}</div>;
}
