import React, { useState, useEffect } from "react";
import {
  Heading,
  Stack,
  Box,
  Flex,
  Button,
  ButtonGroup,
  Link,
  useToast,
} from "@chakra-ui/react";
import { Link as RouterLink } from "react-router-dom";
import { Data } from "../utils.js";
import InputPlaylist from "../components/InputPlaylist.jsx";
import PieChart from "../components/PieChart.jsx";
import BarChart from "../components/BarChart.jsx";
import axios from "axios";

const Visualize = () => {
  const [chartData, setChartData] = useState([]);

  const [userData, setUserData] = useState({
    labels: chartData.map((d) => d.name),
    datasets: [
      {
        label: "Releases",
        data: chartData.map((d) => d.value),
        backgroundColor: ["green"],
      },
    ],
  });

  useEffect(() => {
    console.log(chartData);
    setUserData({
      labels: chartData.map((d) => d.name),
      datasets: [
        {
          label: "Releases",
          data: chartData.map((d) => d.value),
          backgroundColor: ["green"],
        },
      ],
    });
  }, [chartData]);

  return (
    <>
      <Box bg="black" w="100%" h="100%">
        <Stack spacing="2rem" align="center">
          <Heading as="h1" color="Green" fontSize="6xl" mt="3.5rem" mb="4rem">
            Yazify
          </Heading>
          <Flex>
            <ButtonGroup>
              <Link as={RouterLink} to="/">
                <Button backgroundColor="#228B22" color="black" size="lg">
                  Recommend
                </Button>
              </Link>
              <Link as={RouterLink} to="/chart">
                <Button backgroundColor="#228B22" color="black" size="lg">
                  Visualize
                </Button>
              </Link>
            </ButtonGroup>
          </Flex>
          <InputPlaylist setter={setChartData} />
          <Box w="45%" h="45%" mt="4rem">
            <BarChart chartData={userData} />
          </Box>
        </Stack>
      </Box>
    </>
  );
};

export default Visualize;
