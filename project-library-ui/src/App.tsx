import React from 'react';
import { Button, Container, Box  } from '@mui/material';

export const App = () => {
  return (
    <div className="App">
      <Box component="section" sx={{ display: 'flex', p: 2, border: '1px solid grey', justifyContent: 'center'  }}>
        <Button variant="contained" color='primary'> oi Belone </Button>
        <Button variant="contained"> Oi Maria  </Button>
      </Box>
    </div>
  );
}

export default App;