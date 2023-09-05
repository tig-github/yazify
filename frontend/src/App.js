import React, { useState, useEffect } from "react";
import "./App.css";
import { ChakraProvider } from "@chakra-ui/react";
import axios from "axios";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Visualize from "./pages/Visualize.jsx";
import Recommend from "./pages/Recommend.jsx";

function App() {
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
