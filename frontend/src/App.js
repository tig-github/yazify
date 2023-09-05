import React, { useState, useEffect } from "react";
import "./App.css";
import InputSong from "./components/InputSong.jsx";
import Songs from "./components/Songs.jsx";
import PieChart from "./components/PieChart.jsx";
import {
  ChakraProvider,
  Heading,
  Stack,
  Box,
  Flex,
  IconButton,
  useToast,
} from "@chakra-ui/react";
import { RepeatIcon } from "@chakra-ui/icons";
import { Data } from "./utils.js";
import axios from "axios";

function App() {
  const [songs, setSongs] = useState(["Enter a Spotify Song Link"]);

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

  // dev function to refresh database, will later be set in stone
  const refresh = async () => {
    try {
      setSongs(["Updating song database..."]);
      await axios.get(`/refresh`);
      setSongs(["Enter a Spotify Song Link"]);
      console.log("Successful update");
    } catch (error) {
      console.log(error);
      setSongs(["Enter a Spotify Song Link"]);
    }
  };
  const toast = useToast();

  return (
    <ChakraProvider>
      <Box bg="black" w="100%" h="100%">
        <Stack spacing="2rem" align="center">
          <Heading as="h1" color="Green" fontSize="6xl" mt="3.5rem" mb="4rem">
            Yazify
          </Heading>
          <Flex>
            <InputSong setter={setSongs} test={songs} />
            <IconButton
              colorScheme="green"
              variant="outline"
              ml="1rem"
              mt=".25rem"
              _hover={{ borderColor: "#228B22" }}
              _focus={{ borderColor: "#228B22" }}
              _active={{ color: "black", borderColor: "#228B22" }}
              icon={<RepeatIcon />}
              onClick={() => {
                refresh();
                toast({
                  title: "Updating database",
                  description:
                    "Updating song database - this might take some time!",
                  duration: 9000,
                  isClosable: true,
                  status: "info",
                  colorScheme: "green",

                  variant: "subtle",
                });
              }}
            />
          </Flex>
          {songs && <Songs songs={songs} />}
          <Box w="60%" h="100%">
            <PieChart chartData={userData} />
          </Box>
        </Stack>
      </Box>
    </ChakraProvider>
  );
}

export default App;
