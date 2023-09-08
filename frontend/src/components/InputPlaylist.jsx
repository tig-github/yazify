import React, { useState } from "react";
import { Input, useToast } from "@chakra-ui/react";
import axios from "axios";

const InputPlaylist = ({ setter, k }) => {
  const [playlist, setPlaylist] = useState("");

  const handleChange = (event) => {
    const value = event.target.value;
    setPlaylist(value);
  };

  const getPlaylists = async () => {
    try {
      const res = await axios.get(`/visualize?playlist=${playlist}&key=${k}`);
      console.log(`!!!! ${res}`);

      setter(res["data"]);
    } catch (error) {
      console.log(error);
      setter(["Error - request for recommendations failed."]);
    }
  };
  const toast = useToast();

  const handleSubmit = (event) => {
    event.preventDefault();
    toast({
      title: "Getting Chart Data",
      description:
        "Grabbing Chart Data - this takes far longer on playlists that are 1000+ songs. Changing options requires a resubmit.",
      duration: 9000,
      isClosable: true,
      status: "info",
      colorScheme: "green",

      variant: "subtle",
    });
    getPlaylists();
  };

  return (
    <form onSubmit={handleSubmit}>
      <Input
        size="lg"
        borderColor="#228B22"
        color="green"
        type="text"
        _hover={{ color: "#228B22", borderColor: "#228B22" }}
        focusBorderColor="#228B22"
        value={playlist}
        onChange={handleChange}
        placeholder="Enter a spotify playlist"
      ></Input>
    </form>
  ); //will return a form
};

export default InputPlaylist;
