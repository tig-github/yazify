import React, { useState, useEffect } from "react";
import "./App.css";
import InputSong from "./components/InputSong.jsx";
import Songs from "./components/Songs.jsx";
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
import axios from "axios";

function App() {
  const [songs, setSongs] = useState(["Enter a Spotify Song Link"]);

  useEffect(() => {
    console.log(songs);
  }, [songs]);

  const refresh = async () => {
    try {
      setSongs(["Updating song database..."]);
      const res = await axios.get(`/refresh`);
      console.log(res);
      setSongs(["Enter a Spotify Song Link"]);
    } catch (error) {
      console.log(error);
    }
  };
  const toast = useToast();

  return (
    <ChakraProvider>
      <Box bg="black" w="100%" h="calc(100vh)">
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
                  colorScheme: "green",

                  variant: "subtle",
                });
              }}
            />
          </Flex>
          {songs && <Songs songs={songs} />}
        </Stack>
      </Box>
    </ChakraProvider>
  );
}

export default App;
