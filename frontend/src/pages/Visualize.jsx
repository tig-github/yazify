import React, { useState, useEffect } from "react";
import {
  Heading,
  Stack,
  Text,
  Box,
  Flex,
  Button,
  ButtonGroup,
  Select,
  Link,
  useToast,
} from "@chakra-ui/react";
import { Link as RouterLink } from "react-router-dom";
import InputPlaylist from "../components/InputPlaylist.jsx";
import PieChart from "../components/PieChart.jsx";
import BarChart from "../components/BarChart.jsx";

const Visualize = () => {
  const [chartData, setChartData] = useState([]);
  const [chartType, setChartType] = useState("bar");
  const [key, setKey] = useState("releases");

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

  const handleChartChange = (event) => {
    setChartType(event.target.value);
  };

  const handleKeyChange = (event) => {
    setKey(event.target.value);
  };

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
          <InputPlaylist setter={setChartData} k={key} />

          <Flex>
            <Select
              color="#228B22"
              borderColor="#228B22"
              mr="1rem"
              onChange={handleChartChange}
            >
              <option value="bar">Bar Graph</option>
              <option value="pie">Pie Chart</option>
            </Select>
            <Select
              color="#228B22"
              borderColor="#228B22"
              onChange={handleKeyChange}
            >
              <option value="releases">Release Date</option>
              <option value="albums">Album</option>
              <option value="artists">Artist</option>
            </Select>
          </Flex>

          {chartType == "bar" && (
            <Box w="45%" h="45%" mt="4rem">
              <BarChart chartData={userData} />
            </Box>
          )}
          {chartType == "pie" && (
            <Box w="25%" h="25%" mt="4rem">
              <PieChart chartData={userData} />
            </Box>
          )}
          <Box color="Black" h="25vh"></Box>
        </Stack>
      </Box>
    </>
  );
};

export default Visualize;
