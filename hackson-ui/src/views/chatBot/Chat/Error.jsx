import React from "react";
import { Typography } from "@mui/material";

const Error = ({ err }) => {
  return (
    <Typography className="errorMessage" variant="body1">
      An error occurred - "{err.message || 'Failed to fetch'}". Try again later.
    </Typography>
  );
};

export default Error;