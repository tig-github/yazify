import React, { useState, useEffect } from "react";
import { Input } from "@chakra-ui/react";
import axios from "axios";

const InputSong = ({ setter }, { test }) => {
  const [song, setSong] = useState("");

  const handleChange = (event) => {
    const value = event.target.value;
    setSong(value);
  };

  const getSongs = async () => {
    try {
      const res = await axios.get(`/songs?song=${song}`);
      console.log(res);
      //console.log(res["data"]["songs"]);
      setter(res["data"]["songs"]);
    } catch (error) {
      console.log(error);
    }
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    setter(["Generating Song Recommendations"]);
    // now sends song to backend, which then returns a list to render in Songs.jsx
    getSongs();
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
        value={song}
        onChange={handleChange}
      ></Input>
    </form>
  ); //will return a form
};

export default InputSong;
