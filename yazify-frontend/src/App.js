import React, { useState, useEffect } from "react";
import "./App.css";
import InputSong from "./components/InputSong.jsx";
import Songs from "./components/Songs.jsx";
import { ChakraProvider, Heading, Stack, Box } from "@chakra-ui/react";

function App() {
  const [songs, setSongs] = useState([]);

  useEffect(() => {
    alert(songs);
  }, [songs]);

  return (
    <ChakraProvider>
      <Box bg="black" w="100%" h="calc(100vh)">
        <Stack spacing="2rem" align="center">
          <Heading as="h1" color="Green" mt="3.5rem">
            Yazify
          </Heading>
          <InputSong setter={setSongs} />
          <Songs songs={songs} />
        </Stack>
      </Box>
    </ChakraProvider>
  );
}

export default App;
