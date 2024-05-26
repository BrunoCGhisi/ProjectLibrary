import React from 'react';
import { Button, Container, Box  } from '@mui/material';

export const App = () => {
  return (
    <div className="App">
      <Box component="section" sx={{ display: 'flex', p: 2, border: '1px solid grey', justifyContent: 'center'  }}>
        <Button variant="contained" color='primary'> Hello world </Button>
        <Button variant="contained"> Hello world^^2 </Button>
      </Box>
    </div>
  );
}

export default App;

