import React from "react";
import { styled } from '@mui/material/styles';
import { Button, IconButton } from "@mui/material";
import { CloudUpload } from '@mui/icons-material';

const VisuallyHiddenInput = styled('input')`
  clip: rect(0 0 0 0);R
  clip-path: inset(50%);
  height: 1px;
  overflow: hidden;
  position: absolute;
  bottom: 0;
  left: 0;
  white-space: nowrap;
  width: 1px;
`;

const Upload = (props) => {
  const { onUpload, children, ...btnProps } = props;

  const _onUpload = (e) => {
    e.preventDefault();
    const file = e.target.files[0];
    onUpload(file);
  }

  if (children) {
    return (
      <Button
        component="label"
        variant="contained"
        startIcon={<CloudUpload />}
        href="#file-upload"
      >
        {children}
        <VisuallyHiddenInput type="file" onChange={_onUpload} />
      </Button>
    );
  }

  return (
    <IconButton
      component="label"
      variant="contained"
      aria-label="upload"
      title="Upload a file"
      href="#file-upload"
      {...btnProps}
    >
      <CloudUpload />
      <VisuallyHiddenInput type="file" onChange={_onUpload} />
    </IconButton>
  )
};

export default Upload;