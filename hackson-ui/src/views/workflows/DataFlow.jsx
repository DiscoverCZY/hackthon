import React, { useEffect, useState } from 'react';

import {
  Button,
  Box
} from '@mui/material';
import Modal from 'components/Modal';
import { TaskForm } from './Form';

const mockdata = [];

const DataFlow = (props) => {
  const { row, onClose } = props;
  const { name, } = row;

  const [tasks, setTasks] = useState([]);
  const [task, setTask] = useState();
  const getWorkflowList = () => {
    setTasks(null);
    fetch('/api/workflows/tasks', {
      method: 'GET',
      headers: {
        "Content-Type": "application/json"
      },
    }).then(async (response) => {
      const { data } = await response.json();
      setTasks(mockdata);
    }
    ).catch(error => {
      console.error(error);
      setTasks([]);
      setTasks(mockdata);
    });
  };

  useEffect(() => {
    getWorkflowList();
  }, []);

  return (
    <Modal
      key={'dataflow'}
      title={`Workflow: ${name}`}
      fullScreen
      show
      onClose={onClose}
    >
      <Box className="data-flow">
        <Box className="flow">
          dataflow
          <button onClick={() => setTask({ name: 'Task1' })}>open</button>
          <button onClick={() => setTask()}>close</button>
        </Box>
        <Box className={`side${task ? ' open' : ''}`}>
          {
            task && (
              <Box className="task">
                <Box className="title">{task.name || 'Create a task'}</Box>
                <Box className="taskFrom">
                  <TaskForm data={task} />
                </Box>
              </Box>
            )
          }
        </Box>
      </Box>
    </Modal>
  )
};

export default DataFlow;
