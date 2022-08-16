import React from 'react';
import Stack from "@mui/material/Stack";
import Button from '@mui/material/Button';


const Dashboard = () => {
  return (
    <div>
      <Stack direction="row" spacing={1}>
        <Button variant="outlined" border-radius={10}>01</Button>
        <Button variant="outlined">02</Button>
        <Button variant="outlined">03</Button>
      </Stack>

    </div>
    
  )
}

export default Dashboard