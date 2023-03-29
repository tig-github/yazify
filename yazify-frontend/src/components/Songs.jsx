import { React } from "react";
import { UnorderedList, ListItem, Text } from "@chakra-ui/react";

const Songs = ({ songs }) => {
  return (
    <UnorderedList>
      {songs.map((song) => {
        return (
          <ListItem key={song}>
            <Text color="green">{song}</Text>
          </ListItem>
        );
      })}
    </UnorderedList>
  );
};

export default Songs;
