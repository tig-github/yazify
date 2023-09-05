import React, { useState, useEffect } from "react";
import {
  Heading,
  Stack,
  Box,
  Flex,
  IconButton,
  useToast,
} from "@chakra-ui/react";
import { Data } from "../utils.js";
import PieChart from "../components/PieChart.jsx";
import axios from "axios";

const Visualize = () => {
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
  return (
    <>
      <Box bg="black" w="100%" h="100%">
        <Stack spacing="2rem" align="center">
          <Heading as="h1" color="Green" fontSize="6xl" mt="3.5rem" mb="4rem">
            Yazify
          </Heading>
          <Box w="45%" h="45%">
            <PieChart chartData={userData} />
          </Box>
        </Stack>
      </Box>
    </>
  );
};

export default Visualize;
