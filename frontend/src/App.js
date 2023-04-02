import React, { useState, useEffect } from "react";
import "./App.css";
import InputSong from "./components/InputSong.jsx";
import Songs from "./components/Songs.jsx";
import { ChakraProvider, Heading, Stack, Box } from "@chakra-ui/react";

function App() {
  const [songs, setSongs] = useState(["Enter a Spotify Song Link"]);

  useEffect(() => {
    console.log(songs);
  }, [songs]);

  return (
    <ChakraProvider>
      <Box bg="black" w="100%" h="calc(100vh)">
        <Stack spacing="2rem" align="center">
          <Heading as="h1" color="Green" fontSize="6xl" mt="3.5rem" mb="4rem">
            Yazify
          </Heading>
          <InputSong setter={setSongs} test={songs} />
          {songs && <Songs songs={songs} />}
        </Stack>
      </Box>
    </ChakraProvider>
  );
}

export default App;
