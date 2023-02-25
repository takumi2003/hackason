import Home from './Home.jsx';
import { createBrowserRouter, createRoutesFromElements, RouterProvider } from "react-router-dom";
import Sapporo from './sapporo.jsx';

const router = createBrowserRouter([
  {
    path: "/", //url
    element: <Home sapporo_url=""/>, //名前
  },
  {
    path: "sapporo",
    element: <Sapporo/>
  }
]);


const App = () => {
  return <Home/>;
};

export default App;




