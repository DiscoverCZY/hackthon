import React from 'react';
// material-ui
import {
  Box,
} from '@mui/material';

import Pipeline from 'components/Pipeline'

import "./style.css";


const DataPipeline = () => {
  return (
    <Box className="pipeline">
      <Pipeline />
    </Box>
  )
}

export default DataPipeline;