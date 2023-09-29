import React, { useState } from "react";
import InputSong from "../components/InputSong.jsx";
import Songs from "../components/Songs.jsx";
import {
  Heading,
  Stack,
  Box,
  Flex,
  IconButton,
  Button,
  ButtonGroup,
  Link,
  useToast,
} from "@chakra-ui/react";
import { Link as RouterLink } from "react-router-dom";
import { RepeatIcon } from "@chakra-ui/icons";
import axios from "axios";

const Recommend = () => {
  const [songs, setSongs] = useState(["Enter a Spotify Song Link"]);
  let DEBUG_MODE = false;
  const refresh = async () => {
    // dev function to refresh database for debug mode
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
    <>
      <Box bg="black" w="100%" h="calc(100vh)">
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

          <Flex>
            <InputSong setter={setSongs} test={songs} />
            {DEBUG_MODE && (
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
            )}
          </Flex>
          {songs && <Songs songs={songs} />}
        </Stack>
      </Box>
    </>
  );
};

export default Recommend;
