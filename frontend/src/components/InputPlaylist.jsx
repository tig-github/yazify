import React, { useState, useEffect } from "react";
import { Input } from "@chakra-ui/react";
import axios from "axios";

const InputPlaylist = ({ setter }) => {
  const [playlist, setPlaylist] = useState("");
  const [key, setKey] = useState("releases");

  const handleChange = (event) => {
    const value = event.target.value;
    setPlaylist(value);
  };

  const getPlaylists = async () => {
    try {
      const res = await axios.get(`/visualize?playlist=${playlist}&key=${key}`);
      console.log(res);
      //console.log(res["data"]["songs"]);
      setter(res);
    } catch (error) {
      console.log(error);
      setter(["Error - request for recommendations failed."]);
    }
  };

  const handleSubmit = (event) => {
    event.preventDefault();
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
      ></Input>
    </form>
  ); //will return a form
};

export default InputPlaylist;
