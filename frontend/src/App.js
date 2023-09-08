import React from "react";
import "./App.css";
import { ChakraProvider } from "@chakra-ui/react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Visualize from "./pages/Visualize.jsx";
import Recommend from "./pages/Recommend.jsx";

function App() {
  return (
    <ChakraProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Recommend />} />
          <Route path="/chart" element={<Visualize />} />
        </Routes>
      </BrowserRouter>
    </ChakraProvider>
  );
}

export default App;
