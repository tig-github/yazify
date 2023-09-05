import React, { useState, useEffect } from "react";
import "./App.css";
import { ChakraProvider } from "@chakra-ui/react";
import { Data } from "./utils.js";
import axios from "axios";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Recommend from "./pages/Recommend.jsx";
import Visualize from "./pages/Visualize.jsx";

function App() {
  const [userData, setUserData] = useState({
    labels: Data.map((d) => d.year),
    datasets: [
      {
        label: "Users Gained",
        data: Data.map((d) => d.userGain),
        backgroundColor: ["green"],
      },
    ],
  });

  // useEffect(() => {
  //   console.log(songs);
  // }, [songs]);

  return (
    <ChakraProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Recommend />} />
          <Route path="/chart" element={<Visualize />} />
        </Routes>
      </BrowserRouter>
      {/* <Box w="50%" h="80%">
            <PieChart chartData={userData} />
          </Box> */}
    </ChakraProvider>
  );
}

export default App;
