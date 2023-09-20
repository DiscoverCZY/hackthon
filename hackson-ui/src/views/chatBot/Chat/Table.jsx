import React from 'react';

import Table from 'components/table';

const columns = [
  {
    field: 'name',
    label: 'Name',
    align: 'left',
  },
  {
    field: 'progress',
    label: 'Progress',
    width: 300,
  },
  {
    field: 'status',
    label: 'Status',
    width: 100,
  },
];

const ChatTable = (props) => {
  return (
    <Table
      name="Workflows"
      columns={columns}
      height={320}
      {...props}
    />
  )
};

export default ChatTable;