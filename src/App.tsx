import React from 'react';
import { Button, Container, Box  } from '@mui/material';
import menuImage from './assets/libraryMenu.jpg';

export const App = () => {
  return (
    <div className="App">

      <Box component="section" 
      sx={{
        border: '1px solid grey',
        display: 'flex',
        justifyContent: 'center',
        p: '2'
      }}>
        
        <Button variant="contained" color='error'> Criar </Button>
      </Box>

    </div>

  );

}

export default App;


