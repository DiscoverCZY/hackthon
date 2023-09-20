import React, { forwardRef, useState, useImperativeHandle } from 'react';
import {
  Box,
  FormControl,
  FormLabel,
  TextField,
  Select,
  MenuItem,
} from '@mui/material';

const DEFAULT_TASK = {
  name: 'New Task',
  type: 2,
  source: 1,
  path: 1,
  cluster: 2
};

export const TaskForm = forwardRef((props, formRef) => {
  const { data } = props;
  const [formData, setFormData] = useState({...DEFAULT_TASK, ...data});
  const onHandleSubmit = (e) => {
    return formData;
  };

  useImperativeHandle(formRef, () => ({
    onHandleSubmit
  }));

  const onFormChange =(e, type)=>{
    setFormData({
      ...formData,
      [type]: e.target.value
    })
  };

  return (
    <Box component="form" noValidate onSubmit={onHandleSubmit} sx={{ width: 340 }}>
      <FormControl fullWidth id="name" sx={{ mb: 2 }}>
        <FormLabel required>Name</FormLabel>
        <TextField
          required
          defaultValue={DEFAULT_TASK.name}
          onChange={(e)=>onFormChange(e, 'name')}
        />
      </FormControl>
      <FormControl fullWidth id="type" sx={{ mb: 2 }}>
        <FormLabel required>Type</FormLabel>
        <Select
          required
          value={2}
          // onChange={handleChange}
          fullWidth
          // readOnly
        >
          <MenuItem value={1}>NoteBook</MenuItem>
          <MenuItem value={2}>Python Script</MenuItem>
          <MenuItem value={3}>Python whell</MenuItem>
          <MenuItem value={4}>SQL</MenuItem>
          <MenuItem value={5}>Delta Live Table pipeline</MenuItem>
          <MenuItem value={6}>DBT</MenuItem>
          <MenuItem value={7}>JAR</MenuItem>
          <MenuItem value={8}>Spark Submit</MenuItem>
        </Select>
      </FormControl>
      <FormControl fullWidth id="source" sx={{ mb: 2 }}>
        <FormLabel required>Source</FormLabel>
        <Select
          required
          value={1}
          // onChange={handleChange}
          fullWidth
        >
          <MenuItem value={1}>Workspace</MenuItem>
          <MenuItem value={2}>DBFS</MenuItem>
          <MenuItem value={3}>Git Prvider</MenuItem>
        </Select>
      </FormControl>
      <FormControl fullWidth id="path" sx={{ mb: 2 }}>
        <FormLabel required>Path</FormLabel>
        <Select
          required
          value={1}
          // onChange={handleChange}
          fullWidth
        >
          <MenuItem value={1}>Workspace</MenuItem>
          <MenuItem value={2}>DBFS</MenuItem>
          <MenuItem value={3}>Git Prvider</MenuItem>
        </Select>
      </FormControl>
      <FormControl fullWidth id="cluster" sx={{ mb: 2 }}>
        <FormLabel required>Cluster</FormLabel>
        <Select
          required
          value={1}
          // onChange={handleChange}
          fullWidth
        >
          <MenuItem value={1}>Job_cluster</MenuItem>
          <MenuItem value={2}>2</MenuItem>
          <MenuItem value={3}>3</MenuItem>
        </Select>
      </FormControl>
    </Box>
  )
});