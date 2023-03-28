import React, { useState, useEffect } from "react";
import { Input } from "@chakra-ui/react";
import axios from "axios";

const InputSong = (setter) => {
  const [song, setSong] = useState("");

  const handleChange = (event) => {
    const value = event.target.value;
    setSong(value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // now sends song to backend, which then returns a list to render in Songs.jsx
    axios({
      method: "GET",
      url: "songs",
    })
      .then((response) => {
        const res = response.data;
        alert(res);
      })
      .catch((error) => {
        if (error.response) {
          console.log(error.response);
          console.log(error.response.status);
          console.log(error.response.headers);
        }
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <Input
        color="green"
        type="text"
        value={song}
        onChange={handleChange}
      ></Input>
    </form>
  ); //will return a form
};

export default InputSong;
