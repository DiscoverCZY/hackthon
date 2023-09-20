import React from 'react';
// material-ui
import {
  Box,
} from '@mui/material';

import Chat from './Chat';
import Pingpong from 'components/pingpong';

import "./style.css";


const ChatBox = () => {
  return (
    <Box className="chatBot">
      <Box className="side">
        <Pingpong />
        <Box className="bg" />
      </Box>
      <Chat userid={"pingpong"} />
    </Box>
  )
}

export default ChatBox;