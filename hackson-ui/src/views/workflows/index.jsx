import React, { useState, useEffect } from 'react';
// material-ui
import {
  Box,
  Grid,
  Typography,
  Button,
  Alert
} from '@mui/material';
import Add from '@mui/icons-material/Add';


import Table from 'components/table';
import * as Celler from './Celler';
import "./style.css";

const columns = [
  {
    field: 'name',
    label: 'Name',
    align: 'left',
    render: 'Dataflow'
  },
  {
    field: 'progress',
    label: 'Progress',
    width: 300,
    render: 'Progress'
  },
  {
    field: 'status',
    label: 'Status',
    width: 200,
    render: 'Status'
  },
  {
    field: 'startDate',
    label: 'Execution Data',
    width: 200,
  },
  {
    field: 'actions',
    label: 'Actions',
    align: 'center',
    width: 200,
    render: 'Actions'
  },
];

const mockdata = [
  {
    id: 'aa',
    name: 'WF1',
    progress: 30,
    status: 'Running',
    startDate: '9/21/2023',
    test: true
  },
  {
    id: 'bb',
    name: 'WF2',
    progress: 80,
    status: 'Approved',
    startDate: '9/21/2023'
  },
  {
    id: 'cc',
    name: 'WF3',
    progress: 10,
    status: 'Rejected',
    startDate: '9/21/2023'
  },
  {
    id: 'aa',
    name: 'WF1',
    progress: 30,
    status: 'Pending',
    startDate: '9/21/2023'
  },
  {
    id: 'bb',
    name: 'WF2',
    progress: 80,
    status: 'Approved',
    startDate: '9/21/2023'
  },
  {
    id: 'cc',
    name: 'WF3',
    progress: 10,
    status: 'Rejected',
    startDate: '9/21/2023'
  },
  {
    id: 'aa',
    name: 'WF1',
    progress: 30,
    status: 'Pending',
    startDate: '9/21/2023'
  },
  {
    id: 'bb',
    name: 'WF2',
    progress: 80,
    status: 'Approved',
    startDate: '9/21/2023'
  },
  {
    id: 'cc',
    name: 'WF3',
    progress: 10,
    status: 'Rejected',
    startDate: '9/21/2023'
  },
  {
    id: 'aa',
    name: 'WF1',
    progress: 30,
    status: 'Pending',
    startDate: '9/21/2023'
  },
  {
    id: 'bb',
    name: 'WF2',
    progress: 80,
    status: 'Approved',
    startDate: '9/21/2023'
  },
  {
    id: 'cc',
    name: 'WF3',
    progress: 10,
    status: 'Rejected',
    startDate: '9/21/2023'
  },
];

const Workflows = () => {
  const [workflows, setWorkfolows] = useState(null);
  const [alert, setAlert] = useState();

  const handleAlert = (type, msg) => {
    setAlert({
      severity: type,
      children: msg
    });
    const timmer = type === 'success' ? 1000 : 3000;
    setTimeout(() => setAlert(), timmer);
  }

  const getWorkflowList = () => {
    setWorkfolows(null);
    fetch('/api/workflows', {
      method: 'GET',
      headers: {
        "Content-Type": "application/json"
      },
    }).then(async (response) => {
      const { data } = await response.json();
      setWorkfolows(mockdata);
    }
    ).catch(error => {
      console.error(error);
      // handleAlert('error', error.message);
      setWorkfolows([]);
      setWorkfolows(mockdata);
    });
  };

  const handleWorkflowRun = (id) => {
    fetch(`http://localhost:4000/api/workflows/runWorkflow?id=${id}`, {
      method: 'GET',
      headers: {
        "Content-Type": "application/json"
      },
    }).then(async (response) => {
      handleAlert('success', 'Start running');
    }
    ).catch(error => {
      console.error(error);
      // handleAlert('error', error.message);
      handleAlert('success', 'Start running');
    });
  };

  const handleCreate = (type, data) => {
    fetch(`/api/workflows/${type}`, {
      method: 'POST',
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data),
    }).then(async (response) => {
      getWorkflowList();
    }
    ).catch(error => {
      console.error(error);
      // handleAlert('error', error.message);
      getWorkflowList();
    });
  };

  const [openWorkflowCreat, setOpenWorkflowCreat] = React.useState(false);
  const onHandleWorkflowCreate = (v) => {
    setOpenWorkflowCreat(v);
  };

  useEffect(() => {
    getWorkflowList();
  }, []);


  return (
    <Box className="workflows">
      <Grid container alignItems="center" justifyContent="space-between" sx={{ mb: 1 }}>
        <Grid item>
          <Typography variant="h5">Workflow</Typography>
        </Grid>
        {
          alert &&
          <Grid item>
            <Alert {...alert} />
          </Grid>
        }

        <Grid item>
          <Button variant="contained" endIcon={<Add />} onClick={() => onHandleWorkflowCreate(true)}>
            Create
          </Button>
        </Grid>
      </Grid>
      <Table
        name="Workflows"
        columns={columns}
        data={workflows}
        components={{
          ...Celler
        }}
        actions={{
          getWorkflowList,
          handleWorkflowRun,
          handleCreate
        }}
      />
      <Celler.WorkflowCreate
        actions={{
          getWorkflowList,
          handleWorkflowRun,
          handleCreate
        }}
        show={openWorkflowCreat}
        onClose={() => onHandleWorkflowCreate(false)}
      />
    </Box>
  )
}

export default Workflows;